:orphan:

.. title:: BLUETOOTH_H4

.. option:: CONFIG_BLUETOOTH_H4:
.. _CONFIG_BLUETOOTH_H4:

Bluetooth H:4 UART driver. Requires hardware flow control
lines to be available.



:Symbol:           BLUETOOTH_H4
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "H:4 UART" if SERIAL (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_UART_INTERRUPT_DRIVEN` if SERIAL (value: "n")
 *  :option:`CONFIG_BLUETOOTH_UART` if SERIAL (value: "n")
 *  :option:`CONFIG_BLUETOOTH_HOST_BUFFERS` if SERIAL (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:32