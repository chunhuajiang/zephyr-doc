.. _networking_api_usage:

Network 连接 API
########################

应用程序可以使用在 :file:`net_context.h` 中定义的连接 API 来创建连接、发送/接收数据、关闭连接。DUP 和 TCP 数据使用系统的 API。

net_context API 与 BAD socket API 非常相似，它们之间存在一一对应的关系。net_context API 与 BAD socket API 的主要不同是处是 net_context API 使用的是碎片化的网络 buffer（net_buf），而 BSD socket API 使用的是线性内存 buffer。

下面的这个例子创建了一个简单的服务器，它监听发送过来的 UDP 连接并将接收到的数据再送回去。您可以在这里 `connectivity-example-app.c <https://gerrit.zephyrproject.org/r/gitweb?p=zephyr.git;a=blob;f=doc/subsystems/networking/connectivity-example-app.c>`_ 下载这个例子的源码。

例程开始时进行了一些初始化。（这里仅仅是举例；您可以在您自己的应用程序中做一些其它的事儿。）

.. literalinclude:: connectivity-example-app.c
    :linenos:
    :language: c
    :lines: 2-54

初始化后，应用程序需要做的第一件事儿是创建一个 context。context 与 socket 类似。

.. literalinclude:: connectivity-example-app.c
    :linenos:
    :language: c
    :lines: 57-66

然后为连接定义一个本地终点（local end point）。

.. literalinclude:: connectivity-example-app.c
    :linenos:
    :language: c
    :lines: 69-83

等待，直到接收到连接数据。

.. literalinclude:: connectivity-example-app.c
    :linenos:
    :language: c
    :lines: 86-202

完成后，关闭 context。

.. literalinclude:: connectivity-example-app.c
    :linenos:
    :language: c
    :lines: 204-215

.. toctree::
   :maxdepth: 1
