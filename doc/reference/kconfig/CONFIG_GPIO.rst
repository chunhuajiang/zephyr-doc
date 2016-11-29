:orphan:

.. title:: GPIO

.. option:: CONFIG_GPIO:
.. _CONFIG_GPIO:

Include GPIO drivers in system config



:Symbol:           GPIO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO Drivers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_FAMILY_NRF5 && SERIAL && UART_NRF5 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig:19
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:32
 * ../boards/x86/arduino_101/Kconfig.defconfig:21
 * ../boards/x86/galileo/Kconfig.defconfig:13
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:9
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:53
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:24
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:24
 * ../boards/arm/bbc_microbit/Kconfig.defconfig:24
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:24
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:24
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:24
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:24