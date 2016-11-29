:orphan:

.. title:: UART_QMSI_0_HW_FC

.. option:: CONFIG_UART_QMSI_0_HW_FC:
.. _CONFIG_UART_QMSI_0_HW_FC:

The configuration item CONFIG_UART_QMSI_0_HW_FC:

:Symbol:           UART_QMSI_0_HW_FC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HW flow control for UART_0 controller" if UART_QMSI_0 (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_H4 && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:32
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:21
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:34