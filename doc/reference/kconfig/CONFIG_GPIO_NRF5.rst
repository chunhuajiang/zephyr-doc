:orphan:

.. title:: GPIO_NRF5

.. option:: CONFIG_GPIO_NRF5:
.. _CONFIG_GPIO_NRF5:

Enable GPIO driver for nRF5 line of MCUs.



:Symbol:           GPIO_NRF5
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Nordic Semiconductor nRF5X-based GPIO driver" if GPIO && SOC_FAMILY_NRF5 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && SOC_FAMILY_NRF5 (value: "n")
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
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.nrf5:18
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:27
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:27
 * ../boards/arm/bbc_microbit/Kconfig.defconfig:27
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:27
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:27
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:27
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:27