:orphan:

.. title:: BLUETOOTH_MONITOR_ON_DEV_NAME

.. option:: CONFIG_BLUETOOTH_MONITOR_ON_DEV_NAME:
.. _CONFIG_BLUETOOTH_MONITOR_ON_DEV_NAME:

This option specifies the name of UART device to be used
for the Bluetooth monitor logging.



:Symbol:           BLUETOOTH_MONITOR_ON_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of Bluetooth monitor logging UART" if BLUETOOTH_DEBUG_MONITOR (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
 *  "UART_1"
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
 *  "UART_1"
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
 *  "UART_2"
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
 *  UART_QMSI_1_NAME (value: "")
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
 *  UART_QMSI_1_NAME (value: "")
 *   Condition: BLUETOOTH_DEBUG_MONITOR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:315
 * ../arch/x86/soc/ia32/Kconfig.defconfig:104
 * ../arch/x86/soc/atom/Kconfig.defconfig:97
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:83
 * ../boards/x86/arduino_101/Kconfig.defconfig:46
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:46