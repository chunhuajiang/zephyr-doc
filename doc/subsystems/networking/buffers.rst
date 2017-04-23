网络 buffer
###############

网络 buffer 是网络协议栈（以及蓝牙协议栈）中数据传递的核心概念。与他们相关的 API 位于头文件 ``include/net/buf.h`` 中。

.. Hit::

  注：本节中的 `buffer` 和 `缓冲`表示同一个意思，二者相互混用。

创建 buffer
****************

创建网络 buffer 时需要先定义一个缓冲池：

.. code-block:: c

   NET_BUF_POOL_DEFINE(pool_name, buf_count, buf_size, user_data_size, NULL);

缓冲池是一个静态变量，因此如果需要导出到其它模块，需要一个独立的指针。

缓冲池定义好后，我们就可以从它里面分配 buffer：

.. code-block:: c

   buf = net_buf_alloc(&pool_name, timeout);

缓冲池或者缓冲池中的 buffer 没有明确的初始化函数，其初始化是在函数 :c:func:`net_buf_alloc` 被调用时隐式地完成的。

如果需要在 buffer 中为随后的协议头部预留空间，则可以用下面的接口保留 headroom 大小的缓冲空间：

.. code-block:: c

   net_buf_reserve(buf, headroom);

除实际的协议数据和通用解析上下文外，网络缓冲中可能还包含协议相关的上下文 —— 用户数据。buffer 的数据和用户数据容量是在申明缓冲池时（编译时）定义的。

buffer 可以通过内核对象 k_fifo 进行传递。当 buffer 需要从一个线程传递给另一个线程时，这就显得非常适用。不过，由于一个 net_buf 上面可能附着有碎片链，因此当在 FIFO 间传递数据时要使用专用的 API :c:func:`net_buf_put` 和 :c:func:`net_buf_get`，而不要用 :c:func:`k_fifo_put` 和 :c:func:`k_fifo_get`。这些 API 能确保 buffer 链保持完整。

通用操作
*****************

网络 buffer API 为编码/解码 buffer 中的数据提供了有用的助手。为了充分地理解这些助手，最好能理解下面这些基本操作概念：

Add
  
  添加数据到 buffer 的尾部。在保持实际数据指针不懂的同时，修改数据的长度值。需要确保 buffer 中有足够的 tailroom。下面是一些添加数据的 API：

  .. code-block:: c

     void *net_buf_add(struct net_buf *buf, size_t len);
     uint8_t *net_buf_add_u8(struct net_buf *buf, uint8_t value);
     void net_buf_add_le16(struct net_buf *buf, uint16_t value);
     void net_buf_add_le32(struct net_buf *buf, uint32_t value);

Push

  准备数据到 buffer 的头部。既会修改数据指针，又会修改数据长度值。需要确保 buffer 中有足够的 headroom。下面是一些 push 数据的 API：

  .. code-block:: c

     void *net_buf_push(struct net_buf *buf, size_t len);
     void net_buf_push_le16(struct net_buf *buf, uint16_t value);
     uint32_t net_buf_pull_le32(struct net_buf *buf);

Pull
  
  从 buffer 的头部移除数据。既会修改数据指针，又会修改数据长度值。下面是一些 pull 数据的 API：

  .. code-block:: c

     void *net_buf_pull(struct net_buf *buf, size_t len);
     uint8_t net_buf_pull_u8(struct net_buf *buf);
     uint16_t net_buf_pull_le16(struct net_buf *buf);

Add 和 Push 用于将数据编码到 buffer 中去；Pull 用具将数据从 buffer 中解码出来。

引用计数
******************

每个网络 buffer 都有一个引用计数。buffer 最初是通过调用函数 :c:func:`net_buf_alloc()` 从空闲缓冲池中获取得到的，此时的缓冲计数是 1。当调用 :c:func:`net_buf_ref()` 时引用计数递增，调用 :c:func:`net_buf_unref()` 时引用计数递减。当引用计数降至 0 时该 buffer 会被自动放回到空闲缓冲池中。