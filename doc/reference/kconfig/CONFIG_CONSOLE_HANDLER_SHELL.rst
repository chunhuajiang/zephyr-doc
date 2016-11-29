:orphan:

.. title:: CONSOLE_HANDLER_SHELL

.. option:: CONFIG_CONSOLE_HANDLER_SHELL:
.. _CONFIG_CONSOLE_HANDLER_SHELL:

Shell implementation based on CONSOLE_HANDLER.



:Symbol:           CONSOLE_HANDLER_SHELL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable console input handler [ Experimental ]" if CONSOLE_HANDLER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CONSOLE_HANDLER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:42