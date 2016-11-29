:orphan:

.. title:: BLUETOOTH_PRIVACY

.. option:: CONFIG_BLUETOOTH_PRIVACY:
.. _CONFIG_BLUETOOTH_PRIVACY:

Enable local Privacy Feature support. This makes it possible
to use Resolvable Private Addresses (RPAs).



:Symbol:           BLUETOOTH_PRIVACY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Privacy Feature"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN && BLUETOOTH_SMP (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:176