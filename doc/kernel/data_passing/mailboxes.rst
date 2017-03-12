.. _mailboxes_v2:

邮筒
#########

:dfn:`（邮筒）mailbox` 是一个内核对象，它提供了对消息队列对象的增强功能。邮筒允许线程以同步或异步的方式发送和接收任意尺寸的消息。

.. contents::
    :local:
    :depth: 2

概念
********

可以定义任意数量的邮筒。邮筒通过内存地址对其进行引用。

邮筒的关键属性包括：

* **发送队列**：包含已被发送但还未被接收的消息。

* **接收队列**：包含正在等待接收数据的线程。

邮筒必须先初始化再使用。初始化时会将它的所有队列设为空。

邮筒只允许线程（不包括 ISR）交换消息。发送消息的线程叫做 **发送线程**，接收消息的线程叫做 **接收线程**。每个消息只能被一个线程接收（即不支持单点对多点消息和广播消息）。

使用邮筒交换的消息被处理时时非匿名的，它允许参与交换的线程知道（甚至指定）其它线程的标识符。

消息格式
==============

**消息描述符** 是一个数据结构，它指定了消息的位置，以及消息是如何被邮筒处理的。发现线程和接收线程在访问邮筒时都会提供一个消息描述符。邮筒使用消息描述符在相兼容的发送和接收线程间交换消息。在交换期间，邮筒可以更新消息描述符的某些字段，以告诉线程在此期间发生了什么。

一个邮筒消息包含零字节或多个字节的 **消息数据**。消息数据的尺寸和格式是由应用程序指定的，且不同消息的格式也可以不一样。消息数据存在两种形式：

* **消息缓冲**：它是一个由线程提供的一段内存区域，用于发送和接收消息。消息缓冲多数都是由数组变量或结构体变量实现的。

* A **消息块**：它是一段从内存池分配的内存区域。

一个消息 *不能* 同时是消息缓冲和消息块。这两种形式都不是的消息别叫做 **空消息**。

.. note::
    
    如果一个消息存在消息缓冲或者消息块，但是它包含零字节的实际数据，则这样的消息 *不是* 空消息。

消息的生命周期
=================

消息的生命周期是明确的。在发送线程将数据递交给邮筒时，消息就被创建了。之后，消息属于邮筒。再之后，消息被递交给接收线程。接收线程可以在它从邮筒接收到消息时恢复消息数据，也可以在随后的第二次从邮筒接收到消息时才恢复数据。只有当数据被恢复时，邮筒才会删除消息。

线程兼容性
====================

发送线程可以指定接收消息的线程的地址，或者可以通过指定 :c:macro:`K_ANY` 将消息发送给任意线程。类似的，接收线程可以指定从哪个线程接收地址，或者可以通过指定 :c:macro:`K_ANY` 从任何线程接收消息。只有当发送线程和接收线程的需求都被满足时，消息才会被成功地交换；这样的线程被叫做 **兼容的**。

例如，如果线程 A （只）发送给线程 B 发送一个消息，则只有线程 B 希望从线程 A 接收消息或者希望从任意线程接收消息时，消息才会被接收。如果线程 B 希望从线程 C 接收消息，则该消息不会被接收。这个消息不会被线程 C 接收（即使他希望从线程 A 或者任意线程接收消息）。

消息流控制
====================

邮筒消息可以被 **同步** 或者 **异步** 交换。在同步交换中，发送线程在消息被接收线程完全处理前会一直阻塞。在异步交换中，发送线程不会等待消息被另一个线程接收，它会直接继续执行；这样能允许发送线程在将消息给接收线程并完全处理 *前* 执行其它工作（例如收集在下一个消息中需要使用的数据）。

同步交换技术提供了一个隐式的流控制形式，即能阻止发哦是哪个线程产生消息的速度快于接收线程消费的速度。异步交换技术也提供给了一个隐式的流控制形式，即发送消息的线程需要在发送后续消息时判断前一个消息是否仍然存在。

实现
**************

定义邮筒
==================

使用类型为 :c:type:`struct k_mbox` 的变量可以定义一个邮筒。邮筒定义后必须使用函数 :cpp:func:`k_mbox_init()` 对其进行初始化。

下面的代码定义并初始化了一个空邮筒。

.. code-block:: c

    struct k_mbox my_mailbox;

    k_mbox_init(&my_mailbox);

也可以使用宏 :c:macro:`K_MBOX_DEFINE` 在编译时定义和初始化一个邮筒。

下面的代码与上面的代码片段具有相同的作用。

.. code-block:: c

    K_MBOX_DEFINE(my_mailbox);

消息描述符
===================

消息描述符是一个结构为 :c:type:`struct k_mbox_msg` 的类型。只能使用下面所列举的字段；其它的字段仅限于邮筒内部所用。

*info*
 
    被消息发送者和接收者所交换的一个 32 比特的值，它的意义由应用程序定义。这种交换是双向的，即允许发送者在任何消息交换时给接收者传递数据，也允许接收者在同步消息交换时给发送者传递数据。
    
*size*

    消息数据的尺寸，单位是字节。零表示发送一个空的消息或者发送一个无实际数据的消息缓冲或消息块。接收时，将其设为所希望接收数据的最大值，或者如果消息数据不是自己想要的时候将其设为零。当消息被接收后，邮筒会更新这个字段为实际所交换的字节数。
    
*tx_data*
    
    一个执行发送线程消息缓冲的指针。当发送一个内存块或者一个空消息时，将其设为 :c:macro:`NULL`。当接收消息时，让该字段保持未初始化。
    
*tx_block*

    发送线程的内存块的描述符。当发送一个空消息时，将 tx_block.pool_id 设为 :c:macro:`NULL`。当发送一个消息缓冲或者接收一个消息时，将该字段保持未初始化。
    
*tx_target_thread*
    
    
    希望接收消息的线程的地址。将其设为 :c:macro:`K_ANY` 可允许任何线程接收该消息。当接收消息时，让该字段保持未初始化。当消息被接收后，邮筒会将该字段更新为实际接收者的地址。
    
*rx_source_thread*
    
    希望发送线程的地址。将其设为 :c:macro:`K_ANY` 可允许接收任何线程发送的消息。当发送消息时，让该字段保持未初始化。当消息被接收后，邮筒会将该字段更新为实际发送者的地址。

发送消息
=================

线程发送消息时需要先创建消息数据。当数据量很小，且拷贝数据的代价少于分配、释放内存块的代价时，通常会使用消息缓冲。

接着，发送下才能会创建一个用于描述待发送消息的消息描述符，如前一节所述。

最后，发送线程会调用邮筒发送 API 去初始化消息交换的过程。如果存在一个兼容的接收线程，消息会被立即递交给它；否则，消息会被添加的邮筒的发送队列中。

多个消息可以同时存在发送队列中。发送队列中的消息按照发送线程的优先级进行存储。相同优先级的消息按照先进先出的顺序进行存储。

对于同步发送，相关操作会在接收线程接收完消息且恢复完消息数据后完成。如果消息在发送线程所指定的等待时间到达后还未被接收，该消息会被移除邮筒的发送队列，发送失败。当发送成功后，发送线程会检查消息描述符，然后判断是哪个线程接收了消息，有多少数据被交换，以及由接收线程提供的应用程序定义的信息值。

.. note::
   
   同步发送可以导致发送线程被无限期地阻塞（甚至当线程指定了最大等待时间）。等待时间只是限定了邮筒在消息被另一个线程接收前的等待时间。消息被接收后，接收线程恢复消息数据并解除发送线程阻塞状态的时间是 *无限制* 的。
   
对于异步发送，操作总是立即完成。这样可以让发送线程不用理会消息是否立即给了接收线程或者被添加到发送队列中，而继续做其它工作。发送线程可以指定一个信号量，当消息被邮筒删除时（例如消息被接收接收线程所接收，且数据被恢复），邮筒会释放信号量。信号量的使用可以让发送线程轻松实现流控制，确保邮筒在任何时间段都不会持有一个发送线程（或者一系列发送线程）的应用程序所指定的消息数量。

.. note::
   以异步方式发送消息的线程没有办法判断哪个线程接收了消息，由多数消息被交换，以及由接收线程所提供的应用程序定义的信息值。
   
发送空消息
------------------------

这段代码使用邮筒给任何想要数据的线程异步传递了 4 字节的随机数值。消息的 “info” 字段足够运载被交换的消息，因此消息的数据部分不会被使用。

.. code-block:: c

    void producer_thread(void)
    {
        struct k_mbox_msg send_msg;

        while (1) {

            /* generate random value to send */
            uint32_t random_value = sys_rand32_get();

            /* prepare to send empty message */
            send_msg.info = random_value;
            send_msg.size = 0;
            send_msg.tx_data = NULL;
            send_msg.tx_block.pool_id = NULL;
            send_msg.tx_target_thread = K_ANY;

            /* send message and wait until a consumer receives it */
            k_mbox_put(&my_mailbox, &send_msg, K_FOREVER);
        }
    }

使用消息缓冲发送数据
-----------------------------------

这段代码使用邮筒从生产线程给任何想要数据的消费线程同步传递了尺寸可变的请求。消息的 “info” 字段用于传输每个线程可以处理的最大尺寸的消息缓冲。

.. code-block:: c

    void producer_thread(void)
    {
        char buffer[100];
        int buffer_bytes_used;

        struct k_mbox_msg send_msg;

        while (1) {

            /* generate data to send */
            ...
            buffer_bytes_used = ... ;
            memcpy(buffer, source, buffer_bytes_used);

            /* prepare to send message */
            send_msg.info = buffer_bytes_used;
            send_msg.size = buffer_bytes_used;
            send_msg.tx_data = buffer;
            send_msg.tx_target_thread = K_ANY;

            /* send message and wait until a consumer receives it */
            k_mbox_put(&my_mailbox, &send_msg, K_FOREVER);

            /* info, size, and tx_target_thread fields have been updated */

            /* verify that message data was fully received */
            if (send_msg.size < buffer_bytes_used) {
                printf("some message data dropped during transfer!");
                printf("receiver only had room for %d bytes", send_msg.info);
            }
        }
    }

使用消息块发送数据
----------------------------------

这段代码使用邮筒发送异步消息。它使用了一个信号量，让之前的消息被消费后再发送新消息，因此当消费线程不能够消费时，积压的消息不会增加。

消息数据储存于从内存池中获取的内存块中，因此当交换大消息时能消除不必要的数据拷贝。内存池只包含两块：其中一块被填充着数据，先前被发送的另一块则正在被处理。

.. code-block:: c

    /* define a semaphore, indicating that no message has been sent */
    K_SEM_DEFINE(my_sem, 1, 1);

    /* define a memory pool containing 2 blocks of 4096 bytes */
    K_MEM_POOL_DEFINE(my_pool, 4096, 4096, 2, 4);

    void producer_thread(void)
    {
        struct k_mbox_msg send_msg;

        volatile char *hw_buffer;

        while (1) {
            /* allocate a memory block to hold the message data */
            k_mem_pool_alloc(&mp_pool, &send_msg.tx_block, 4096, K_FOREVER);

            /* keep overwriting the hardware-generated data in the block    */
            /* until the previous message has been received by the consumer */
            do {
                memcpy(send_msg.tx_block.data, hw_buffer, 4096);
            } while (k_sem_take(&my_sem, K_NO_WAIT) != 0);

            /* finish preparing to send message */
            send_msg.size = 4096;
            send_msg.tx_target_thread = K_ANY;

            /* send message containing most current data and loop around */
            k_mbox_async_put(&my_mailbox, &send_msg, &my_sem);
        }
    }

接收消息
===================

线程通过接收消息时，它会先创建一个用于描述它所希望接收的消息的消息描述符，然后调用某个邮筒接收 API。邮筒会搜索它的发送队列，并从它搜索到的第一个兼容线程中取出消息。如果没有兼容线程，接收线程可以等待。如果在接收线程所指定的等待时间到达之前仍然没有兼容线程出现，则接收失败。接收完成后，接收线程可以检查消息的描述符，以查看是哪个线程发送的消息，有多少数据被交互，以及发送线程提供的应用程序相关的信息值。

多个接收线程可以同时等待在一个邮筒的接收队列上。这些线程以优先级进行排序；相同优先级的线程以先进先出的顺序进行排序。

.. note::
    
    由于消息描述符会指定线程兼容性，所以接收线程并非总是按照先进先出（FIFO）的顺序接收到数据的。例如，如果线程 A 希望从线程 X 接收消息，线程 B 希望从线程 Y 接收线程，此时如果有一个来自线程 Y 的发送给任意线程的消息到来，这线程 B 会接收到该消息，线程 A 则继续等待。


接收线程会同时控制从到达消息恢复数据时的数据数量和数据的结束之处。线程可以获取消息中的所有数据，也可以获取部分数据或者不获取任何数据。类似地，线程也可以让数据拷贝到某个消息缓冲中，也可以让数据放到某个消息块中。消息缓冲通常用于当数据量很小导致拷贝数据的代价小于分配、释放内存池块的代码时。

下面几小结总结了接收线程在恢复消息数据时的各种方法。

在接收时恢复数据
-------------------------------

线程恢复消息数据的最直接的方法是当消息到达时指定一个消息缓冲：该缓冲的位置（不能是 :c:macro:`NULL` ）和尺寸。

邮筒会将消息的数据拷贝到这个消息缓冲中。如果消息缓冲不够容纳所有的消息数据，未被拷贝的将被丢失。如果消息缓冲大于消息数据的尺寸，则消息缓冲中未被使用的部分将保持不变。无论是在那种情况下，邮筒都会更新接收线程的消息描述符，以指示具体有多少字节的数据被拷贝。

立即数据恢复技术通常用于消息量很小（能提前知道消息的最大尺寸）的情况。

.. note::

   当发送线程提供的消息数据位于内存块时，也可以使用这种技术。邮筒会将数据拷贝到接收线程所指定的消息缓冲中，然后将消息块释放回内存池。这样的好处是接收线程不需要知道数据是由消息块发送的还是由消息缓冲发送的。

下面的代码利用了数据立即恢复技术，它使用邮筒来处理来自生产线程的尺寸可变的请求。消息的 “info” 字段用于交换每个线程可以处理的消息缓冲的最大尺寸。

.. code-block:: c

    void consumer_thread(void)
    {
        struct k_mbox_msg recv_msg;
        char buffer[100];

        int i;
        int total;

        while (1) {
            /* prepare to receive message */
            recv_msg.info = 100;
            recv_msg.size = 100;
            recv_msg.rx_source_thread = K_ANY;

            /* get a data item, waiting as long as needed */
            k_mbox_get(&my_mailbox, &recv_msg, buffer, K_FOREVER);

            /* info, size, and rx_source_thread fields have been updated */

            /* verify that message data was fully received */
            if (recv_msg.info != recv_msg.size) {
                printf("some message data dropped during transfer!");
                printf("sender tried to send %d bytes", recv_msg.info);
            }

            /* compute sum of all message bytes (from 0 to 100 of them) */
            total = 0;
            for (i = 0; i < recv_msg.size; i++) {
                total += buffer[i];
            }
        }
    }

随后使用消息缓冲恢复数据
--------------------------------------------

当消息被接收后，接收先可以推迟恢复消息数据的时间，即它可以在随后的一段时间再将数据恢复到消息缓冲中。要利用这种功能，线程需要指定消息缓冲的位置为 :c:macro:`NULL`，以及它所希望恢复的数据的最大尺寸。

邮筒不会拷贝任何消息数据。不过，邮筒仍然会更新接收线程的消息描述符，以指示有多少字节的数据可用于恢复。

接收线程必须按如下方式进行响应：

* 如果消息描述符的尺寸是零，表示发送者的消息没包含任何数据或者接收线程不需要接收任何数据。接收线程不需要做任何动作，因为邮筒内部已经完成了数据恢复和消息删除。

* 如果消息描述符的尺寸非零，且接收线程仍然希望恢复数据，则该线程必须调用 :cpp:func:`k_mbox_data_get()`，并提供一个足够容纳数据的消息缓冲。邮筒会将数据拷贝到消息缓冲并删除消息。

* 如果消息描述符的尺寸非零，且接收线程 **不** 向接收数据，则该线程必须调用 :cpp:func:`k_mbox_data_get()`，并将消息缓冲指定为 :c:macro:`NULL`。邮筒不会拷贝数据，会直接删除消息。

数据的随后恢复技术适用于当应用程序不适合立即恢复的场景。例如，当由于内存限制导致接收线程不能够提供一个能够容纳达到消息数据的消息缓冲时。

.. note::

   当发送线程提供的消息数据位于内存块时，也可以使用这种技术。邮筒会将数据拷贝到接收线程所指定的消息缓冲中，然后将消息块释放回内存池。这样的好处是接收线程不需要知道数据是由消息块发送的还是由消息缓冲发送的。

下面的代码使用了邮筒的数据延迟恢复计数来获取从生产线程发送的消息数据。由于只有当消息满足某个标准时才会恢复数据，因此能减小不必要的数据拷贝。发送者指定的消息的 “info” 字段用于区分消息的类别。

.. code-block:: c

    void consumer_thread(void)
    {
        struct k_mbox_msg recv_msg;
        char buffer[10000];

        while (1) {
            /* prepare to receive message */
            recv_msg.size = 10000;
            recv_msg.rx_source_thread = K_ANY;

            /* get message, but not its data */
            k_mbox_get(&my_mailbox, &recv_msg, NULL, K_FOREVER);

            /* get message data for only certain types of messages */
            if (is_message_type_ok(recv_msg.info)) {
                /* retrieve message data and delete the message */
                k_mbox_data_get(&recv_msg, buffer);

                /* process data in "buffer" */
                ...
            } else {
                /* ignore message data and delete the message */
                k_mbox_data_get(&recv_msg, NULL);
            }
        }
    }

随后使用消息块恢复数据
-------------------------------------------

接收线程可以将消息数据恢复到一个内存块（而非消息缓冲）中。这种方法与在随后使用消息缓冲恢复数据的方法基本 —— 接收线程先接收消息（不带数据），然后调用函数 :cpp:func:`k_mbox_data_block_get()` 恢复数据。邮筒会填充接收线程提供的消息描述符，允许线程访问数据。当数据被恢复后，邮筒会删除消息。然后，接收线程在不需要数据时负责释放将消息块释放回内存池中。

这种技术更适用于消息数据由内存块发送的应用程序。

.. note::
   
   当发送线程的消息数据位于消息缓冲时，也可以利用这种技术。邮筒会自动分配一个内存块并将数据拷贝到里面。不过，这种方法比直接将数据恢复到由接收线程提供的消息缓冲更低效。此外，接收线程在必须够处理当由于邮筒不能分配到内存块而导致数据恢复失败的情形。如果这种情况发送了，接收线程必须尝试在随后再次恢复数据，或者指示邮筒删除消息（没有恢复数据）。

下面的代码使用邮筒来接收一个由内存块发送的消息，因此可以消除不必要的内存拷贝（尤其是大消息）。消息可能被同步发送，也可能被异步发送。

.. code-block:: c

    /* define a memory pool containing 1 block of 10000 bytes */
    K_MEM_POOL_DEFINE(my_pool, 10000, 10000, 1, 4);

    void consumer_thread(void)
    {
        struct k_mbox_msg recv_msg;
        struct k_mem_block recv_block;

        int total;
        char *data_ptr;
        int i;

        while (1) {
            /* prepare to receive message */
            recv_msg.size = 10000;
            recv_msg.rx_source_thread = K_ANY;

            /* get message, but not its data */
            k_mbox_get(&my_mailbox, &recv_msg, NULL, K_FOREVER);

            /* get message data as a memory block and discard message */
            k_mbox_data_block_get(&recv_msg, &my_pool, &recv_block, K_FOREVER);

            /* compute sum of all message bytes in memory block */
            total = 0;
            data_ptr = (char *)(recv_block.data);
            for (i = 0; i < recv_msg.size; i++) {
                total += data_ptr++;
            }

            /* release memory block containing data */
            k_mem_pool_free(&recv_block);
        }
    }

.. note::
    
    这种算法也能正确地处理使用消息缓冲发送的消息，以为邮筒会自动从内存池中分配一个内存块，并使用消息数据填充它。不过，这样的会丢失性能。

建议的用法
**************

当消息队列不足以在两个线程间传递数据时，使用邮筒。

配置选项
*********************

相关的配置选项：

* :option:`CONFIG_NUM_MBOX_ASYNC_MSGS`

API
****

头文件 file:`kernel.h` 提供了如下的邮筒 API：

* :c:macro:`K_MBOX_DEFINE`
* :cpp:func:`k_mbox_init()`
* :cpp:func:`k_mbox_put()`
* :cpp:func:`k_mbox_async_put()`
* :cpp:func:`k_mbox_get()`
* :cpp:func:`k_mbox_data_get()`
* :cpp:func:`k_mbox_data_block_get()`
