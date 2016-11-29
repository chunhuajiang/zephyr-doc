:orphan:

.. title:: BLUETOOTH_H5

.. option:: CONFIG_BLUETOOTH_H5:
.. _CONFIG_BLUETOOTH_H5:

Bluetooth three-wire (H:5) UART driver. Implementation of HCI
Three-Wire UART Transport Layer.



:Symbol:           BLUETOOTH_H5
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "H:5 UART [EXPERIMENTAL]" if SERIAL (value: "n")
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
 * ../drivers/bluetooth/hci/Kconfig:42