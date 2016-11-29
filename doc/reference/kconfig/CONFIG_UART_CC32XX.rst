:orphan:

.. title:: UART_CC32XX

.. option:: CONFIG_UART_CC32XX:
.. _CONFIG_UART_CC32XX:

This option enables the CC32XX UART driver, for UART_0.



:Symbol:           UART_CC32XX
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "CC32XX UART driver" if SOC_SERIES_CC32XX && SOC_FAMILY_TISIMPLELINK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_SERIES_CC32XX && SOC_FAMILY_TISIMPLELINK (value: "n")
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if SOC_SERIES_CC32XX && SOC_FAMILY_TISIMPLELINK (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.cc32xx:1