:orphan:

.. title:: UART_QMSI_1_NAME

.. option:: CONFIG_UART_QMSI_1_NAME:
.. _CONFIG_UART_QMSI_1_NAME:

This option holds the UART_1 device name. If unsure, use the
default name.



:Symbol:           UART_QMSI_1_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART_1 device name" if UART_QMSI_1 (value: "n")
:Default values:

 *  "UART_1"
 *   Condition: UART_QMSI_1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:45