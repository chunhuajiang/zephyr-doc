:orphan:

.. title:: BLUETOOTH_RX_STACK_SIZE

.. option:: CONFIG_BLUETOOTH_RX_STACK_SIZE:
.. _CONFIG_BLUETOOTH_RX_STACK_SIZE:

Size of the receiving thread stack. This is the context from
which all event callbacks to the application occur. The
default value is sufficient for basic operation, but if the
application needs to do advanced things in its callbacks that
require extra stack space, this value can be increased to
accommodate for that.



:Symbol:           BLUETOOTH_RX_STACK_SIZE
:Type:             int
:Value:            "1024"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1024, 65536]
 *  [1024, 65536]
:Prompts:

 *  "Size of the receiving thread stack"
 *  "Size of the receiving thread stack"
:Default values:

 *  1024 (value: "n")
 *   Condition: (none)
 *  1024 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:72
 * ../subsys/bluetooth/host/Kconfig:113