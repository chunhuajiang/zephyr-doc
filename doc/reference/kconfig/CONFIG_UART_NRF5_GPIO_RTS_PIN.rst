:orphan:

.. title:: UART_NRF5_GPIO_RTS_PIN

.. option:: CONFIG_UART_NRF5_GPIO_RTS_PIN:
.. _CONFIG_UART_NRF5_GPIO_RTS_PIN:

The GPIO pin to use for RTS.



:Symbol:           UART_NRF5_GPIO_RTS_PIN
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

 *  "RTS Pin Number" if UART_NRF5 && GPIO_NRF5 && UART_NRF5_FLOW_CONTROL (value: "n")
:Default values:

 *  12 (value: "n")
 *   Condition: (none)
 *  5 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: (none)
 *  12 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:84
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:39
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:39
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:39
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:39
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:39
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:39