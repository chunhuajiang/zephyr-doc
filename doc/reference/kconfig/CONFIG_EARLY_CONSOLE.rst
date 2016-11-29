:orphan:

.. title:: EARLY_CONSOLE

.. option:: CONFIG_EARLY_CONSOLE:
.. _CONFIG_EARLY_CONSOLE:

This option will enable stdout as early as possible, for debugging
purpose. For instance, in case of STDOUT_CONSOLE being set it will
initialize its driver earlier than normal, in order to get the stdout
sent through the console at the earliest stage possible.



:Symbol:           EARLY_CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Send stdout at the earliest stage possible"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BOOT_BANNER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:204