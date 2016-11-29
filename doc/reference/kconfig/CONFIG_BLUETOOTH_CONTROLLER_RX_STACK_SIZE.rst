:orphan:

.. title:: BLUETOOTH_CONTROLLER_RX_STACK_SIZE

.. option:: CONFIG_BLUETOOTH_CONTROLLER_RX_STACK_SIZE:
.. _CONFIG_BLUETOOTH_CONTROLLER_RX_STACK_SIZE:

Size of the receiving thread stack. This is the context from
which all radio messages are encoded into HCI events or data
before passing it to Bluetooth receiving thread.



:Symbol:           BLUETOOTH_CONTROLLER_RX_STACK_SIZE
:Type:             int
:Value:            "256"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [256, 65536]
:Prompts:

 *  "Size of the receiving thread stack"
:Default values:

 *  256 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_CONTROLLER && BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../subsys/bluetooth/controller/Kconfig:32