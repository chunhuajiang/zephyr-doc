:orphan:

.. title:: UART_NRF5_GPIO_CTS_PIN

.. option:: CONFIG_UART_NRF5_GPIO_CTS_PIN:
.. _CONFIG_UART_NRF5_GPIO_CTS_PIN:

The GPIO pin to use for CTS.


:Symbol:           UART_NRF5_GPIO_CTS_PIN
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

 *  "CTS Pin Number" if UART_NRF5 && GPIO_NRF5 && UART_NRF5_FLOW_CONTROL (value: "n")
:Default values:

 *  14 (value: "n")
 *   Condition: (none)
 *  7 (value: "n")
 *   Condition: (none)
 *  10 (value: "n")
 *   Condition: (none)
 *  10 (value: "n")
 *   Condition: (none)
 *  10 (value: "n")
 *   Condition: (none)
 *  10 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_NRF5 && BOARD_ARDUINO_101_BLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:93
 * ../boards/arm/96b_nitrogen/Kconfig.defconfig:42
 * ../boards/arm/nrf52_pca10040/Kconfig.defconfig:42
 * ../boards/arm/nrf51_pca10028/Kconfig.defconfig:42
 * ../boards/arm/quark_se_c1000_ble/Kconfig.defconfig:42
 * ../boards/arm/nrf51_blenano/Kconfig.defconfig:42
 * ../boards/arm/arduino_101_ble/Kconfig.defconfig:42