:orphan:

.. title:: UART_QMSI_0_BAUDRATE

.. option:: CONFIG_UART_QMSI_0_BAUDRATE:
.. _CONFIG_UART_QMSI_0_BAUDRATE:

This option sets the baud rate from the UART_0 device.



:Symbol:           UART_QMSI_0_BAUDRATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART_0 baud rate" if UART_QMSI_0 (value: "n")
:Default values:

 *  115200 (value: "n")
 *   Condition: UART_QMSI_0 (value: "n")
 *  1000000 (value: "n")
 *   Condition: (none)
 *  1000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_H4 && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:25
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:18
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:31