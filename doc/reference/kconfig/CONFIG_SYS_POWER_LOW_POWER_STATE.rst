:orphan:

.. title:: SYS_POWER_LOW_POWER_STATE

.. option:: CONFIG_SYS_POWER_LOW_POWER_STATE:
.. _CONFIG_SYS_POWER_LOW_POWER_STATE:

This option enables the kernel to interface with a power manager
application.  This permits the system to enter a custom CPU low power
state when the kernel becomes idle. The low power state could be any of
the CPU low power states supported by the processor.  Generally the one
saving most power.



:Symbol:           SYS_POWER_LOW_POWER_STATE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Low power state" if MICROKERNEL && SYS_POWER_MANAGEMENT && SYS_POWER_LOW_POWER_STATE_SUPPORTED (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: MICROKERNEL && SYS_POWER_MANAGEMENT && SYS_POWER_LOW_POWER_STATE_SUPPORTED (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SYS_POWER_MANAGEMENT (value: "n")
:Locations:
 * ../kernel/Kconfig:240