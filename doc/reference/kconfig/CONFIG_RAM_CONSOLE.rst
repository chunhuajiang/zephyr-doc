:orphan:

.. title:: RAM_CONSOLE

.. option:: CONFIG_RAM_CONSOLE:
.. _CONFIG_RAM_CONSOLE:

Emit console messages to a RAM buffer "ram_console" which can
be examined at runtime with a debugger. Useful in board bring-up
if there aren't any working serial drivers.



:Symbol:           RAM_CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use RAM console"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CONSOLE_HAS_DRIVER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:112