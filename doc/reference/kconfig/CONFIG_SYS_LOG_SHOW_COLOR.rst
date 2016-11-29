:orphan:

.. title:: SYS_LOG_SHOW_COLOR

.. option:: CONFIG_SYS_LOG_SHOW_COLOR:
.. _CONFIG_SYS_LOG_SHOW_COLOR:

Use color in the logs. This requires an ANSI capable terminal.



:Symbol:           SYS_LOG_SHOW_COLOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use colored logs" if SYS_LOG (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SYS_LOG (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_LOG && BLUETOOTH_DEBUG_COLOR (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:284