网络缓冲
###############

网络缓冲（Network Buffer）是理解网络协议栈（以及蓝牙协议栈）中数据是传递过程的核心概念。相关的 API 位于 ``include/net/buf.h`` 。

创建缓冲
================

创建网络缓冲时需要先申明一个缓冲池：

.. code-block:: c

   static struct nano_fifo free_fifo;
   static NET_BUF_POOL(pool_name, buf_count, buf_size, &free_fifo, NULL,
                       user_data_size);

在进行相关操作前，还需要在运行时对其进行初始化：

.. code-block:: c

   net_buf_pool_init(pool_name);

完成初始化后，协议栈将使用 nano_fifo 对象来管理可用的 buffer。可以这样获得 buffer：

.. code-block:: c

   buf = net_buf_get(&free_fifo, reserve_headroom);

除实际的协议数据和通用解析上下文之外，网络缓冲还包含协议相关的上下文（被叫做用户数据）。缓冲的最大数据容量和用户数据功能都是在声明缓冲池的时候进行定义的。

由于空闲缓冲使用 nano_fifo 进行管理，
Since the free buffers are managed with the help of a nano_fifo it means
the buffers have native support for being passed through other nano_fifos
as well. This is a very practical feature when the buffers need to be
passed from one fiber to another.

通用操作
=================

网络缓冲 API 对将数据编码到缓冲中/从缓冲中解码数据提供了有用的帮助。要完全理解这些帮帮助，最好能理解这些操作中所使用到的基本术语：

添加
  将数据添加到缓冲的末尾。修改数据长度值；保持实际的数据指针不动。确保缓冲的尾部有足够的空间。利用 API 添加数据的一些例子：
  
  .. code-block:: c

     void *net_buf_add(struct net_buf *buf, size_t len);
     uint8_t *net_buf_add_u8(struct net_buf *buf, uint8_t value);
     void net_buf_add_le16(struct net_buf *buf, uint16_t value);
     void net_buf_add_le32(struct net_buf *buf, uint32_t value);

Push
  
  追加数据到缓冲的头部。既修改数据的长度值，又修改数据指针。确保缓冲的头部有足够的空间。利用 API push 数据的一些例子：
  
  .. code-block:: c

     void *net_buf_push(struct net_buf *buf, size_t len);
     void net_buf_push_le16(struct net_buf *buf, uint16_t value);
     uint32_t net_buf_pull_le32(struct net_buf *buf);

Pull
  从缓冲的头部移除数据。既修改数据的长度值，又修改数据指针。利用 API pull 数据的一些例子：

  .. code-block:: c

     void *net_buf_pull(struct net_buf *buf, size_t len);
     uint8_t net_buf_pull_u8(struct net_buf *buf);
     uint16_t net_buf_pull_le16(struct net_buf *buf);

添加和 push 操作用于将数据编码到缓冲中；pull 操作用于从缓冲中解码数据。

引用计数
==================

每个网络缓冲都有一个引用计数。调用函数  :c:func:`net_buf_get()` 可以从空闲缓冲池中请求并初始化一个缓冲，此时该缓冲的引用计数是 1。函数 :c:func:`net_buf_ref()` 用于将引用计数递增；函数 :c:func:`net_buf_unref()` 用于将引用计数递减。到计数降至 0，该缓冲会被自动放回空闲缓冲池中。
