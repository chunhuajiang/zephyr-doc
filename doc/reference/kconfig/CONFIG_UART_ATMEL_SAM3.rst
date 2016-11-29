:orphan:

.. title:: UART_ATMEL_SAM3

.. option:: CONFIG_UART_ATMEL_SAM3:
.. _CONFIG_UART_ATMEL_SAM3:

This option enables the UART driver for Atmel SAM3
family processors. Note that there is only one
UART controller on SAM3. It has only two wires
for RX and TX, and does not have other pins
(such as CTS and RTS).



:Symbol:           UART_ATMEL_SAM3
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 family processor UART driver" if SOC_ATMEL_SAM3 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_ATMEL_SAM3 (value: "n")
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if SOC_ATMEL_SAM3 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.atmel_sam3:1