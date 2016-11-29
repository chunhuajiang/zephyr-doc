:orphan:

.. title:: UART_QMSI_1_BAUDRATE

.. option:: CONFIG_UART_QMSI_1_BAUDRATE:
.. _CONFIG_UART_QMSI_1_BAUDRATE:

This option sets the baud rate from the UART_1 device.



:Symbol:           UART_QMSI_1_BAUDRATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART_1 baud rate" if UART_QMSI_1 (value: "n")
:Default values:

 *  115200 (value: "n")
 *   Condition: UART_QMSI_1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:53