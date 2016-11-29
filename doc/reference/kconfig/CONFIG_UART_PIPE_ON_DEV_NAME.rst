:orphan:

.. title:: UART_PIPE_ON_DEV_NAME

.. option:: CONFIG_UART_PIPE_ON_DEV_NAME:
.. _CONFIG_UART_PIPE_ON_DEV_NAME:

This option specifies the name of UART device to be used
for pipe UART.



:Symbol:           UART_PIPE_ON_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of UART Device for pipe UART" if UART_PIPE (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: UART_PIPE (value: "n")
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_2"
 *   Condition: UART_PIPE (value: "n")
 *  UART_QMSI_1_NAME (value: "")
 *   Condition: (none)
 *  UART_QMSI_1_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_PIPE && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/console/Kconfig:167
 * ../arch/x86/soc/ia32/Kconfig.defconfig:99
 * ../arch/x86/soc/atom/Kconfig.defconfig:92
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:80
 * ../boards/x86/arduino_101/Kconfig.defconfig:41
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:41