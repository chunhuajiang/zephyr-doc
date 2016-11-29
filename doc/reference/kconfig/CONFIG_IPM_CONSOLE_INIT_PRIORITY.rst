:orphan:

.. title:: IPM_CONSOLE_INIT_PRIORITY

.. option:: CONFIG_IPM_CONSOLE_INIT_PRIORITY:
.. _CONFIG_IPM_CONSOLE_INIT_PRIORITY:

Device driver initialization priority.
Console has to be initialized after the IPM subsystem
it uses.



:Symbol:           IPM_CONSOLE_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IPM console init priority" if IPM_CONSOLE_SENDER || IPM_CONSOLE_RECEIVER (value: "n")
:Default values:

 *  60 (value: "n")
 *   Condition: IPM_CONSOLE_SENDER || IPM_CONSOLE_RECEIVER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:146