:orphan:

.. title:: BLUETOOTH_DEBUG_COLOR

.. option:: CONFIG_BLUETOOTH_DEBUG_COLOR:
.. _CONFIG_BLUETOOTH_DEBUG_COLOR:

Use color in the logs. This requires an ANSI capable terminal.



:Symbol:           BLUETOOTH_DEBUG_COLOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use colored logs" if BLUETOOTH_DEBUG_LOG (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: BLUETOOTH_DEBUG_LOG (value: "n")
:Selects:

 *  :option:`CONFIG_SYS_LOG_SHOW_COLOR` if BLUETOOTH_DEBUG_LOG (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:307