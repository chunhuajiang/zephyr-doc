:orphan:

.. title:: UART_NRF5_GPIO_RX_PIN

.. option:: CONFIG_UART_NRF5_GPIO_RX_PIN:
.. _CONFIG_UART_NRF5_GPIO_RX_PIN:

The GPIO pin to use for RX.



:Symbol:           UART_NRF5_GPIO_RX_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 31]
:Prompts:

 *  "RX Pin Number" if UART_NRF5 && GPIO_NRF5 (value: "n")
:Default values:

 *  15 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: (none)
 *  25 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:76
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:36
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:36
 * ../boards/arm/bbc_microbit/Kconfig.defconfig:36
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:36
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:36
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:36
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:36