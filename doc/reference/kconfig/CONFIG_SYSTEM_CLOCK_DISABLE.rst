:orphan:

.. title:: SYSTEM_CLOCK_DISABLE

.. option:: CONFIG_SYSTEM_CLOCK_DISABLE:
.. _CONFIG_SYSTEM_CLOCK_DISABLE:

This option enables the sys_clock_disable() API in the kernel. It is
needed by some subsystems (which will automatically select it), but is
rarely needed by applications.



:Symbol:           SYSTEM_CLOCK_DISABLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "API to disable system clock"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 REBOOT (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:152