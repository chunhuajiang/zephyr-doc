:orphan:

.. title:: SYS_POWER_MANAGEMENT

.. option:: CONFIG_SYS_POWER_MANAGEMENT:
.. _CONFIG_SYS_POWER_MANAGEMENT:

This option enables the board to implement extra power management
policies whenever the kernel becomes idle. The kernel informs the
power management subsystem of the number of ticks until the next kernel
timer is due to expire.



:Symbol:           SYS_POWER_MANAGEMENT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Power management"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:227