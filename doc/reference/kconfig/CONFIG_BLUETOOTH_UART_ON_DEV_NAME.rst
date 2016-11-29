:orphan:

.. title:: BLUETOOTH_UART_ON_DEV_NAME

.. option:: CONFIG_BLUETOOTH_UART_ON_DEV_NAME:
.. _CONFIG_BLUETOOTH_UART_ON_DEV_NAME:

This option specifies the name of UART device to be used
for Bluetooth.



:Symbol:           BLUETOOTH_UART_ON_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of UART Device for Bluetooth" if BLUETOOTH_UART (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: BLUETOOTH_UART (value: "n")
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: (none)
 *  "UART_1"
 *   Condition: BLUETOOTH_UART (value: "n")
 *  UART_QMSI_0_NAME (value: "")
 *   Condition: (none)
 *  UART_QMSI_0_NAME (value: "")
 *   Condition: (none)
 *  "UART_4"
 *   Condition: BLUETOOTH_UART (value: "n")
 *  "UART_3"
 *   Condition: BLUETOOTH_UART (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:80
 * ../arch/x86/soc/ia32/Kconfig.defconfig:85
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:280
 * ../arch/x86/soc/atom/Kconfig.defconfig:85
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:77
 * ../boards/x86/arduino_101/Kconfig.defconfig:34
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:28
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:90
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:90