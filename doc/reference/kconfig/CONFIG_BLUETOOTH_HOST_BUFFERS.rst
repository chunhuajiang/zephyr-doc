:orphan:

.. title:: BLUETOOTH_HOST_BUFFERS

.. option:: CONFIG_BLUETOOTH_HOST_BUFFERS:
.. _CONFIG_BLUETOOTH_HOST_BUFFERS:

Enable this to have the host stack manage incoming ACL data
and HCI event buffers. This makes sense for all HCI drivers
that talk to a controller running on a different CPU.

If the controller resides in the same address space it may
make sense to have the lower layers manage these buffers, in
which case this option can be left disabled.



:Symbol:           BLUETOOTH_HOST_BUFFERS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Host managed incoming data buffers"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H4 || BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H5 || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_CONTROLLER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../drivers/bluetooth/hci/Kconfig:62