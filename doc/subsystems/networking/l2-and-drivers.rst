.. _l2_and_drivers:

L2 协议栈和驱动程序
####################

L2 协议栈的主要设计目的是在上层 IP 协议栈中隐藏整个网络链路部分和相关设备驱动程序。这通过一个叫做“网络接口对象”的唯一标识符实现的：在 `include/net/net_if.h`
中定义的 :c:type:`struct net_if`。

IP 层不需要知道 net_if 对象内部的实现细节。头文件 `include/net/net_l2.h` 中为 L2 层提供的通用 API 包含在结构提 :c:type:`struct net_l2` 中。

只有 L2 层（链接在 net_if 对象内部）能与设备驱动程序对话。L2 层规定了设备驱动程序需要为该设备提供的 API。

当前，L2 层包括 Ethernet、IEEE 802.15.4 Soft-MAC、Bluetooth IPSP 和一个虚拟分层（该分层可以作为添加新分层时的模板分层）。

L2 层的 API
************

要创建一个 L2 层，或者甚至只是为某个指定的 L2 层创建一个驱动程序，您需要明白 IP 层是如何与该层进行交互的，以及 L2 层应该怎样表现。通用的 L2 API 包括三个函数：

- 接收 recv：所有的设备驱动程序，一旦它们接收到一个放到某个 :c:type:`struct net_nbuf` 中的报文，它们会通过函数 :c:func:`net_recv_data()` 将该 buffer push 到 IP 层核心协议栈。但从这点看，IP 核心协议栈并不知道该如何处理这个 buffer。相反，它会沿着 L2 协议栈的 recv() 函数传递 buffer。L2 协议栈会做它应该做的操作，例如解析链路层头部或者处理链路层报文。如果是一个错误的报文，recv() 函数将会返回 NET_DROP；如果是一个能被 L2 正确地消耗的报文，则返回 NET_OK；如果该报文需要 IP 协议栈继续处理，则返回 NET_CONTINUE.

- 保留 reserve：在创建任何网络 buffer 上下文前，Zephyr 的核心协议栈需要知道 L2 层需要多少专用 buffer 空间（例如链路层头部的空间）。该保留函数返回需要的字节数。

- 发送 send：与 recv 类似，IP 核心协议栈需要调用该函数来实际发送数据。所有相关的链路层上下文都会产生并添加到这个函数中。
As for recv, send returns a
  verdict and can decide to drop the packet via NET_DROP if something
  wrong happened, or will return NET_OK.

网络设备驱动程序
**********************

网络设备程序完全遵循 Zephyr 设备驱动程序模型，请参考 :ref:`device_drivers`。

不过，有两处不同：

- driver_api 指针必须指向一个有效的 :c:type:`struct net_if_api` 指针。

- 网络设备驱动程序必须使用 NET_DEVICE_INIT_INSTANCE()。这个宏会调用宏 DEVICE_AND_API_INIT()，并实例化一个与所创建的设备驱动实例相关的唯一 :c:type:`struct net_if`。

实现一个网络设备驱动程序依赖于 L2 协议栈：Ethernet、IEEE 802.15.4 等。在下一节中，我们将讲解设备驱动程序在收发报文时是如何运作的。剩下的东西都是与硬件相关的，因此我们没有必要在这里详细讲解。

Ethernet 设备驱动程序
======================

接收数据时，由设备驱动程序负责将数据填充到 buffer 以及后续分片中。buffer 本身是一个 :c:type:`struct net_nbuf`，由函数 :c:func:`net_nbuf_get_reserve_rx(0)` 进行分配。所有的后续分片也通过函数 :c:func:`net_nbuf_get_reserve_data(0)` 进行分配。当然，所需分片的数量由所接收到报文的大小和每个分片的大小决定。分片的大小由配置选项 `CONFIG_NET_NBUF_DATA_SIZE` 指定。

注意，设备驱动程序并不负责决定在 buffer 中保留多少链路层空间。因此，上面传递的参数是 0。当报文的以太网头部被正确解析后，以太网的 L2 层会更新这些信息。

如果调用函数 :c:func:`net_recv_data()` 失败，则由设备驱动程序通过 :c:func:`net_nbuf_unref()` 解除对 buffer 的引用。

发送数据时，由设备驱动程序立即发送 buffer 及其所有分片。

在所有报文成功传输后，设备驱动程序必须通过 :c:func:`net_nbuf_unref()` 解除对 buffer 的引用。

最后，每个 Ethernet 设备驱动程序需要像这样调用 `NET_DEVICE_INIT_INSTANCE()`：

.. code-block:: c

   NET_DEVICE_INIT_INSTANCE(...,
                            CONFIG_ETH_INIT_PRIORITY
			    &the_valid_net_if_api_instance,
			    ETHERNET_L2,
			    NET_L2_GET_CTX_TYPE(ETHERNET_L2), 1500);

IEEE 802.15.4 设备驱动程序
===========================

IEEE 802.15.4 L2 的设备驱动程序与 Ethernet 的基本一致。上面所描述的，尤其是接收数据，可以很好地适用于此处。不过，仍然有两处不同：

- 它需要一个专用的设备驱动程序 API： :c:type:`struct ieee802154_radio_api`，它比 :c:type:`struct net_if_api` 提供了更多的功能。这是因为 802.15.4 L2 除收发数据的函数外，还需要一些驱动的函数。这个专用 API 定义在头文件 `include/net/ieee802154_radio.h` 中。所有的 IEEE 802.15.4 设备驱动程序都需要填充该 API 结构体。

- 发送报文有一点点特殊。IEEE 802.15.4 发送的帧最多只有 127 字节，包括：枕头、载荷和帧校验和。buffer 分片需要满足这种帧大小限制。
但是一个包含 IPv6/UDP 报文的 buffer 可能包含一个或多个分片。在 Ethernet 设备驱动程序中，是由驱动程序负责处理所有分片的。但是 IEEE 802.15.4 驱动程序依次只能
处理一个分片。这就是为什么 :c:type:`struct ieee802154_radio_api` 需要一个与 :c:type:`struct net_if_api` 不同更多的 tx 函数指针。
相反，IEEE 802.15.4 L2 提供了一个通用的 :c:func:`ieee802154_radio_send()` 作为 :c:type:`struct net_if` 的发送函数。因此，实现 :c:func:`ieee802154_radio_send()` 时
需要确保具有相同的行为：通过 tx 函数 :c:type:`struct ieee802154_radio_api` 每次发送一个分片，仅当所有传输都完成后再解除对 buffer 的引用。

最后，每个 IEEE 802.15.4 设备驱动程序需要像这样调用 `NET_DEVICE_INIT_INSTANCE()`：

.. code-block:: c

   NET_DEVICE_INIT_INSTANCE(...,
                            the_device_init_prio,
			    &the_valid_ieee802154_radio_api_instance,
			    IEEE802154_L2,
			    NET_L2_GET_CTX_TYPE(IEEE802154_L2), 125);
