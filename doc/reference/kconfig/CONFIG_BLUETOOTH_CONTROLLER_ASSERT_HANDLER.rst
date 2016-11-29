:orphan:

.. title:: BLUETOOTH_CONTROLLER_ASSERT_HANDLER

.. option:: CONFIG_BLUETOOTH_CONTROLLER_ASSERT_HANDLER:
.. _CONFIG_BLUETOOTH_CONTROLLER_ASSERT_HANDLER:

This option enables an application-defined sink for the
controller assertion mechanism. This must be defined in
application code as void \"bt_controller_assert_handle(char \*, int)\"
and will be invoked whenever the controller code encounters
an unrecoverable error.




:Symbol:           BLUETOOTH_CONTROLLER_ASSERT_HANDLER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Bluetooth Controller Assertion Handler" if BLUETOOTH_HCI_RAW (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_CONTROLLER && BLUETOOTH_CONTROLLER (value: "n")
:Locations:
 * ../subsys/bluetooth/controller/Kconfig:41