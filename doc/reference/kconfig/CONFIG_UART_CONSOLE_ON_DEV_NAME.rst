:orphan:

.. title:: UART_CONSOLE_ON_DEV_NAME

.. option:: CONFIG_UART_CONSOLE_ON_DEV_NAME:
.. _CONFIG_UART_CONSOLE_ON_DEV_NAME:

This option specifies the name of UART device to be used for
UART console.



:Symbol:           UART_CONSOLE_ON_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of UART Device for UART Console" if UART_CONSOLE (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_CONSOLE (value: "n")
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: USB_UART_CONSOLE = n (value: "y")
 *  "CDC_ACM"
 *   Condition: USB_UART_CONSOLE (value: "n")
 *  "UART_1"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_CONSOLE && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/console/Kconfig:68
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:211
 * ../arch/arc/soc/em11d/Kconfig.defconfig:214
 * ../arch/arc/soc/em7d/Kconfig.defconfig:214
 * ../arch/arc/soc/em9d/Kconfig.defconfig:212
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:219
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:273