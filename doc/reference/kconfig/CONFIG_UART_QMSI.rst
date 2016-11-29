:orphan:

.. title:: UART_QMSI

.. option:: CONFIG_UART_QMSI:
.. _CONFIG_UART_QMSI:

This option enables the QMSI UART driver.

This driver is simply a shim driver based on the UART driver
provided by the QMSI BSP.



:Symbol:           UART_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI UART driver" if QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI (value: "n")
:Selects:

 *  :option:`CONFIG_SERIAL_HAS_DRIVER` if QMSI (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.qmsi:1