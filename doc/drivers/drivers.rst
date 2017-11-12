.. _device_drivers:

设备驱动和设备模型
###############################

介绍
************
Zephyr 内核支持大量的设备驱动程序。应用程序板级配置的可用设备驱动集合随着所关联的硬件组件和设备驱动软件的变化而变化。


Zephyr 的设备模型为配置驱动程序提供了一致的设备模型。设备模型负责初始化配置到系统中的所有驱动。


每种类型的驱动程序（UAR，SPI，I2C）都有一个通用类型的 API。 

在这个模型中，当驱动程序初始化时，驱动中会填充指向包含指向它的 API 函数的结构的指针。这些结构体被按照初始化等级放到 RAM 区。


标准驱动
****************

所有的板级配置中都支持的设备驱动包括：

* **中断控制器**：用于内核的中断管理子系统。

* **定时器**：用于内核的系统时钟和硬件时钟子系统。

* **串行通信**：用于内核的系统控制台子系统。

* **随机数生产器**：提供随机数源。

  .. important::

    这种设备驱动的确切实现并不会产生真正意义上的随机数，只是一个近似随机的数。

同步调用
*****************

Zephyr 对多种板子提供了一系列的设备驱动程序。除非硬件不支持，否则每个驱动都应当提供基于中断（而不是轮询）的实现。

通过上层的设备API来调用这些驱动, 例如 i2c.h spi.h, 他们通常被特意设计为同步操作, 这些调用会产生阻塞.

驱动程序 API
******************

:file:`device.h` 中提供了如下关于设备驱动程序的 API。这些 API 只能用于设备驱动程序中，不能应用于应用程序中。
.

:c:func:`DEVICE_INIT()`
   
   创建设备对象，并在启动的初始化阶段调用其初始化函数。
   
:c:func:`DEVICE_AND_API_INIT()`

   创建设备对象，并在启动的初始化阶段调用其初始化函数。此外，它还用一个指针指向驱动程序的 API。
   
:c:func:`DEVICE_NAME_GET()`
   
   获得一个全局设别对象的全名。
   
:c:func:`DEVICE_GET()`
 
   通过名字获取一个执行设备对象的指针。
   
:c:func:`DEVICE_DECLARE()`
   
   声明一个设备对象。

驱动的数据结构
**********************

设备驱动宏中的某些数据结构分为只读部分和运行时可变部分。在最顶层包括：

.. code-block:: C

  struct device {
        struct device_config *config;
        void *driver_api;
        void *driver_data;
  };

成员 `config` 是只读配置数据的集合，它在编译时就确定了，例如 IO 地址映射的内存、IRQ 号或者设备的其它固定物理特性。这是传递给宏  `DEVICE_*INIT()` 的 `config_info` 结构体。

`driver_data` 结构被置于 ARM 中，它是每个实例在运行时的驱动程序所使用的数据。例如，引用计数、信号量、scratch 缓冲等。

`driver_api` 结构是驱动程序中实现的设备相关的通用子系统 API。它通常是只读的，并在编译时就确定了。在下一节中将详细描述这一点。

子系统以及 API 结构
*****************************

大多数驱动程序的主要目标是提供一个与设备独立的子系统 API。应用程序只需要简单地使用这些通用 API，而不需要了解驱动实现的细节。

子系统 API 的定义通常是这样的：

.. code-block:: C

  typedef int (*subsystem_do_this_t)(struct device *device, int foo, int bar);
  typedef void (*subsystem_do_that_t)(struct device *device, void *baz);

  struct subsystem_api {
        subsystem_do_this_t do_this;
        subsystem_do_that_t do_that;
  };

  static inline int subsystem_do_this(struct device *device, int foo, int bar)
  {
        struct subsystem_api *api;

        api = (struct subsystem_api *)device->driver_api;
        return api->do_this(device, foo, bar);
  }

  static inline void subsystem_do_that(struct device *device, void *baz)
  {
        struct subsystem_api *api;

        api = (struct subsystem_api *)device->driver_api;
        api->do_that(device, foo, bar);
  }

通常，在遇到错误时，除非在某个常规操作中需要返回值（例如存储设备满了），否则最好使用宏 `__ASSERT()` 进行断言。参数错误、编程错误、一致性检查、不可恢复的错误等都需要使用断言进行处理。

当需要返回错误状态给调用者检查时，如果成功则返回 0，如果失败则返回 POSIX errno.h 代码。更多细节请参考 https://wiki.zephyrproject.org/view/Coding_conventions#Return_Codes。


当实现一个具体的子系统时，驱动程序需要定义这些 API，并将它与子系统 API 结构绑定在一起：

.. code-block:: C

  static int my_driver_do_this(struct device *device, int foo, int bar)
  {
        ...
  }

  static void my_driver_do_that(struct device *device, void *baz)
  {
        ...
  }

  static struct subsystem_api my_driver_api_funcs = {
        .do_this = my_driver_do_this,
        .do_that = my_driver_do_that
  };

然后，驱动程序需要将 `my_driver_api_funcs` 作为 `api` 参数传递给宏 `DEVICE_AND_API_INIT()`，或者在驱动的初始化函数中手动地将其赋值给 `device->driver_api`。

.. note::

        由于指向 API 函数的指针是通过 `driver_api` 结构引用的，这些指针将始终被包含到二进制文件中（即使未使用）。链接选项 `gc-sections` 至少能看到对它们的一个引用。当有驱动程序 API 时，如果需要提供链接时的尺寸优化，则通常需要借助于 Kconfig 选项来动态控制可选特性。

单驱动多实例
*********************************

某些驱动程序在一个给定的系统中可能被实例化多次。例如由多个 GPIO 组或者多个 UART。驱动程序的每个实例都会使用不同的 `config_info` 结构和 `driver_data` 结构。


为多驱动实例配置中断是个例外。如果每个实例需要配置一个不同的中断号，可以通过每个实例的配置函数完成，因为传递给 `IRQ_CONNECT()` 的参数会在编译时被解析。

例如，我们需要为 `my_driver` 配置两个实例，每个实例使用一个不同的中断号。在 `drivers/subsystem/subsystem_my_driver.h` 中：


.. code-block:: C

  typedef void (*my_driver_config_irq_t)(struct device *device);

  struct my_driver_config {
        uint32_t base_addr;
        my_driver_config_irq_t config_func;
  };

通用初始化函数中的实现：

.. code-block:: C

  void my_driver_isr(struct device *device)
  {
        /* Handle interrupt */
        ...
  }

  int my_driver_init(struct device *device)
  {
        const struct my_driver_config *config = device->config->config_info;

        /* Do other initialization stuff */
        ...

        config->config_func(device);

        return 0;
  }

当有特殊实例被申明时：

.. code-block:: C

  #if CONFIG_MY_DRIVER_0

  DEVICE_DECLARE(my_driver_0);

  static void my_driver_config_irq_0
  {
        IRQ_CONNECT(MY_DRIVER_0_IRQ, MY_DRIVER_0_PRI, my_driver_isr,
                    DEVICE_GET(my_driver_0), MY_DRIVER_0_FLAGS);
  }

  const static struct my_driver_config my_driver_config_0 = {
        .base_addr = MY_DRIVER_0_BASE_ADDR;
        .config_func = my_driver_config_irq_0;
  }

  static struct my_driver_data_0;

  DEVICE_AND_API_INIT(my_driver_0, MY_DRIVER_0_NAME, my_driver_init,
                      &my_driver_data_0, &my_driver_config_0, SECONDARY,
                      MY_DRIVER_0_PRIORITY, &my_driver_api_funcs);

  #endif /* CONFIG_MY_DRIVER_0 */

注意，使用 `DEVICE_DECLARE()` 时避免循环依赖。

初始化等级
*********************

驱动程序可能会依赖其它先初始化的驱动或者需要使用内核服务。 DEVICE_INIT() 允许用户指定在系统启动的哪个时间段执行设备驱动的初始化函数。所有的驱动程序都需要在如下的五个初始化等级中指定一个：

`PRE_KERNEL_1`
        
        用于那些没有任何依赖的设备，例如那些纯粹只需要处理器/SoC 上的硬件的设备。这些设备在配置期间不需要使用任何内内核服务，因此此时内核服务还未启动。不过，中断子系统会被配置，因此可以设置中断。在这个等级上的初始化函数运行在中断栈上面。

`PRE_KERNEL_2`

        用于那些依赖于已被初始化的 `PRE_KERNEL_1` 等级的设备的设备。这些设备在配置期间不使用任何内核服务，因此此时内核服务还未启动。在这个等级上的初始化函数运行在中断栈上面。
        
`POST_KERNEL`

        用于那些在配置期间需要依赖内核服务的设备。在这个等级上的初始化函数运行在内核主栈的上下文中。

`APPLICATION`

        用于需要自动配置的应用程序组件（即非内核组件）。这些设别在配置期间可以使用内核提供的所有服务。在这个等级上的初始化函数运行在内核主栈的上下文中。
        

在每个初始化等级，您还需要指定一个优先级，用于区分相同初始化等级的其它设备。这个优先级是 0 到 99 之间的整数值。优先级越低表示越早被初始化。优先级必须是一个前面没有补零的或者没有符号的十进制整数字面量或者一个对等的符号（例如 `\#define MY_INIT_PRIO 32`）。符号表达式是不被允许的（例如 `CONFIG_KERNEL_INIT_PRIORITY_DEFAULT + 5`）。


系统驱动
**************

在某些情况下，您可以只需要在启动时运行某个函数。宏 `SYS_INIT` 被映射为 `DEVICE_INIT()` 或 `DEVICE_INIT_PM()`。对于 `SYS_INIT()`，它不存在配置或者运行时的数据结构，因此也不能再随后通过名字获取到设备指针。它的初始化等级和优先级与普通设备是一样的。


对于 `SYS_INIT_PM()`，您可以通过名字获得指针。参考 :ref:`power management
<power_management>` 一节。

:c:func:`SYS_INIT()`

:c:func:`SYS_INIT_PM()`
