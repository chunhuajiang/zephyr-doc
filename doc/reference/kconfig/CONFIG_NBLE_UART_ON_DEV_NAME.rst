:orphan:

.. title:: NBLE_UART_ON_DEV_NAME

.. option:: CONFIG_NBLE_UART_ON_DEV_NAME:
.. _CONFIG_NBLE_UART_ON_DEV_NAME:

This option specifies the name of UART device to be used
for Nordic BLE.



:Symbol:           NBLE_UART_ON_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of UART Device for Nordic BLE" if NBLE (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: NBLE (value: "n")
 *  "UART_1"
 *   Condition: (none)
 *  UART_QMSI_0_NAME (value: "")
 *   Condition: (none)
 *  UART_QMSI_0_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NBLE && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:119
 * ../arch/x86/soc/ia32/Kconfig.defconfig:92
 * ../boards/x86/arduino_101/Kconfig.defconfig:27
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:15