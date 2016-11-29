:orphan:

.. title:: ENABLE_SHELL

.. option:: CONFIG_ENABLE_SHELL:
.. _CONFIG_ENABLE_SHELL:

Enabling shell services. If it is enabled, kernel shell commands are
also available for use.



:Symbol:           ENABLE_SHELL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shell support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/shells/Kconfig:2