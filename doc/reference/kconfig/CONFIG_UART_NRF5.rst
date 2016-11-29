:orphan:

.. title:: UART_NRF5

.. option:: CONFIG_UART_NRF5:
.. _CONFIG_UART_NRF5:

This option enables the UART driver for Nordic Semiconductor nRF5
family processors. Note that there is only one
UART controller on nRF5 ICs.



:Symbol:           UART_NRF5
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Nordic Semiconductor NRF5 family processor UART driver" if SOC_FAMILY_NRF5 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_FAMILY_NRF5 (value: "n")
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if SOC_FAMILY_NRF5 (value: "n")
 *  :option:`CONFIG_GPIO` if SOC_FAMILY_NRF5 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nrf5:18