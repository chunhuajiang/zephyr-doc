:orphan:

.. title:: UART_NRF5_GPIO_TX_PIN

.. option:: CONFIG_UART_NRF5_GPIO_TX_PIN:
.. _CONFIG_UART_NRF5_GPIO_TX_PIN:

The GPIO pin to use for TX.



:Symbol:           UART_NRF5_GPIO_TX_PIN
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

 *  "TX Pin Number" if UART_NRF5 && GPIO_NRF5 (value: "n")
:Default values:

 *  13 (value: "n")
 *   Condition: (none)
 *  6 (value: "n")
 *   Condition: (none)
 *  24 (value: "n")
 *   Condition: (none)
 *  9 (value: "n")
 *   Condition: (none)
 *  9 (value: "n")
 *   Condition: (none)
 *  9 (value: "n")
 *   Condition: (none)
 *  9 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:68
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:33
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:33
 * ../boards/arm/bbc_microbit/Kconfig.defconfig:33
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:33
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:33
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:33
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:33