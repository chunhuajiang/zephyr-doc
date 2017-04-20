.. _NATS_Client_Sample:


NATS 客户端实现示例
#################################


概览
********

`NATS <http://nats.io/documentation/internals/nats-protocol/>`__ 是一个基于 TCP 实现的发布者/订阅者协议。 规范文档在 `NATS Protocol documentation <http://nats.io/documentation/internals/nats-protocol/>`__ 中，这是一个在Zephyr中使用新的IP栈实现的示例。此API是在 `Golang API <https://github.com/nats-io/go-nats>`__基础上的松散实现。

在此示例中，可以针对指定主题进行订阅/注销，并且为异步通知更改。为了节省资源，此实现不会持续跟踪订阅主题；必须由应用程序本身执行，所以它可以忽略未知的/不想要的主题。

虽然基于认证，但还未能支持 TLS。如果回调函数在 ``struct nats`` 中设置，客户端将指示它是否支持用户名/密码。  调用此回调函数时，用户必须将用户名/密码拷贝到所提供的user/pass缓冲。

内容也可能为指定主题发布。

示例应用程序观察主题 “led0”，并 “on打开” 或 “off关闭” 它，或 “toggle切换” 它的值。如果支持，更改值将作用于开发板上的状态 LED，新状态将被发布。

另外值得注意的是，绝大多数的网络和 GPIO 样板已经无耻地抄袭 IRC BOT 的例子。（奇怪的是，这两个协议是相似的）

需求
************

测试示例，要在你的平台上创建 Zephyr 应用。此示例仅在由 Zephyr SDK 所提供的 QEMU 模拟器上测试进行过测试。但它将支持其它硬件，只要这些硬件有足够的内存，网络协议栈支持TCP，并且支持硬件连接。

至于软件，已使用官方 `gnatsd <https://github.com/nats-io/gnatsd>`__ 为服务器端, 和官方`go-nats <https://github.com/nats-io/go-nats>`__ 为客户端进行过测试。建立服务器和客户端的每个指令都可以在它们各自的``README.md`` 文件中找到。

客户端是一个一次性测试，基本上和 ``go-nats`` README 文件中的`Basic Usage
<https://github.com/nats-io/go-nats/blob/e6bb81b5a5f37ef7bf364bb6276e13813086c6ee/README.md#basic-usage>`__ 章节所提供的代码相同。无论如何，此示例的订阅主题为: ``led0``, 发布值为之前描述的 (``on``, ``off``, 和 ``toggle``).

库的使用
*************

为 ``struct nats`` 分配足够的空间，设置一些回调函数作为事件发生的通知：

::

    struct nats nats_ctx = {
        .on_auth_required = on_auth_required,
        .on_message = on_message
    };

``on_auth_required()`` 和 ``on_message()`` 函数作为应用程序的一部分，它们必须具有如下签名:

::

    int on_auth_required(struct nats *nats, char **user, char **pass);
    int on_message(struct nats *nats, struct nats_msg *msg);

两个函数都应当返回0以表明它们可以成功处理自己的角色，任何原因的失败，都应当返回负数。为了易于调试，推荐使用errno.h中所提供的负整数。

第一个函数 ``on_auth_required()``, 它在服务器通告需要认证时被调用。如果不是这样的话，不会被调用，所以它是可选的。无论如何，如果服务器要求证书，而此函数无法提供，连接将关闭，错误由``nats_connect()``返回。

第二个函数 ``on_message()``, 它在服务器被通告值改变时调用。 ``struct nats_msg`` 有如下成员：

::

    struct nats_msg {
        const char *subject;
        const char *sid;
        const char *reply_to;
    };

为了发布一个对此消息的回应，字段 ``reply_to`` 可直接传递给 ``nats_publish()``。如果它为空（从服务器传来的消息中无reply_to字段）,``nats_publish()`` 函数将不会回应一个指定邮箱，仅仅更新主题值。

为管理话题订阅，可使用如下函数:

::

    int nats_subscribe(struct nats *nats, const char *subject,
        const char *queue_group, const char *sid);

``subject`` 和 ``sid``需要是可用的，以便它们在实际的协议规则内有效。如果不是，则返回``-EINVAL``。

如果 ``queue_group``为空, 它不会向服务器发送。

::

    int nats_unsubscribe(struct nats *nats, const char *sid,
        size_t max_msgs);

``sid`` 需要是可用的，以便它们在实际的协议规则内有效。如果不是，则返回``-EINVAL``。

``max_msgs`` 指定了服务器在实际退订消息前将要发送的消息数量。可设置为0以立即退订（参考下面的“注意”部分。）

如果不能创建信息并发送到服务器，所有这些函数都将返回 ``-ENOMEM``。它们也可以返回任意 ``net_context_send()`` 所可以返回的错误。

注意:  为了节省资源，库的实现不会记录订阅的主题。``nats_subscribe()`` 和 ``nats_unsubscribe()`` 函数仅通知服务器：客户端对特定主题是否有兴趣。可通过使用``on_message()``回调函数来通告那些未被订阅（或近期被退订）主题的改变。是否忽略消息，由应用程序决定。

可使用以下函数发布主题:

::

    int nats_publish(struct nats *nats, const char *subject,
        const char *reply_to, const char *payload,
        size_t payload_len);

和之前一样， ``subject`` 需要是有效的，如果为无效格式，将返回``-EINVAL``。 ``reply_to`` 字段可以为 ``NULL``，在这种情况下，此主题的订阅用户也不会收到这些信息

对于 ``net_subscribe()`` 和 ``net_unsubscribe()`` 函数，它们可返回 ``-ENOMEM``，或任意 ``net_context_send()`` 函数所返回的错误。
