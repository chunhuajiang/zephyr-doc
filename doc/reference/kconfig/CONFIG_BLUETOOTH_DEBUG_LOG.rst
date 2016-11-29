:orphan:

.. title:: BLUETOOTH_DEBUG_LOG

.. option:: CONFIG_BLUETOOTH_DEBUG_LOG:
.. _CONFIG_BLUETOOTH_DEBUG_LOG:

This option enables Bluetooth debug going to standard
serial console.



:Symbol:           BLUETOOTH_DEBUG_LOG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Normal printf-style to console"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_BLUETOOTH_DEBUG`
 *  :option:`CONFIG_STDOUT_CONSOLE`
 *  :option:`CONFIG_SYS_LOG`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:280