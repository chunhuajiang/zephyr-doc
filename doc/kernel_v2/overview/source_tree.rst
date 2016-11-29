.. _source_tree_v2:

源码树结构
#####################

理解 Zephyr 源码树有助于快速定位 Zephyr 相关功能的代码。

Zephyr 源码树提供了如下顶层目录，且每个目录可能还包括一个或多个子目录：

:file:`arch`
    架构相关的内核以及 SoC 相关的代码。每个所支持的架构（例如 x86 和 ARM）
	都有一个自己的子目录。每个子目录还包括如下功能的子目录：

    * 架构相关的内核源文件
    * 架构相关的内核头文件和私有 API
    * SoC 相关的代码

:file:`boards`
    开发板相关的代码和配置文件。
    Board related code and configuration files.

:file:`doc`
    Zephyr 文档的源文件和工具。

:file:`drivers`
    设备驱动的代码。

:file:`ext`
    集成到 Zephyr 中的外部源代码，例如厂商提供的硬件接口代码、密码库代码等。

:file:`fs`
    文件系统的代码。

:file:`include`
    
    除 :file:`lib` 外的所公有 API 的头文件。

:file:`kernel`
    架构无关的内核代码。

:file:`lib`
    包括最小化 C 库在内的库代码。

:file:`misc`
    不属于如何顶层目录的杂项代码。

:file:`net`
    网络相关的代码，包括蓝牙协议栈和网络协议栈。

:file:`samples`
    演示 Zephyr 功能特性的应用程序例程。

:file:`scripts`
    各种程序以及用于编译、测试 Zephyr 应用程序的其它文件。

:file:`tests`
    Zephyr 功能特性的测试代码。

:file:`usb`
    USB 设备栈的代码。
