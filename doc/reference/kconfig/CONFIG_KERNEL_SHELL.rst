:orphan:

.. title:: KERNEL_SHELL

.. option:: CONFIG_KERNEL_SHELL:
.. _CONFIG_KERNEL_SHELL:

This shell provides access to basic kernel data like version, uptime
and other useful information.




:Symbol:           KERNEL_SHELL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable kernel shell"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ENABLE_SHELL && CONSOLE (value: "n")
:Locations:
 * ../drivers/console/shells/Kconfig:12