:orphan:

.. title:: BLUETOOTH_INTERNAL_STORAGE

.. option:: CONFIG_BLUETOOTH_INTERNAL_STORAGE:
.. _CONFIG_BLUETOOTH_INTERNAL_STORAGE:

When selected the application doesn't need to register its own
persistent storage handlers through the bt_storage API, rather
an internal default handler is used for this.



:Symbol:           BLUETOOTH_INTERNAL_STORAGE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use an internal persistent storage handler" if FILE_SYSTEM (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:105