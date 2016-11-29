:orphan:

.. title:: CONSOLE_HANDLER_SHELL_STACKSIZE

.. option:: CONFIG_CONSOLE_HANDLER_SHELL_STACKSIZE:
.. _CONFIG_CONSOLE_HANDLER_SHELL_STACKSIZE:

Stack size for the console handler shell.



:Symbol:           CONSOLE_HANDLER_SHELL_STACKSIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Console handler shell stack size" if CONSOLE_HANDLER_SHELL (value: "n")
:Default values:

 *  2000 (value: "n")
 *   Condition: CONSOLE_HANDLER_SHELL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:50