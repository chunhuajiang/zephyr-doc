:orphan:

.. title:: SYS_POWER_DEEP_SLEEP

.. option:: CONFIG_SYS_POWER_DEEP_SLEEP:
.. _CONFIG_SYS_POWER_DEEP_SLEEP:

This option enables the kernel to interface with a power manager
application. This permits the system to enter a Deep sleep state
supported by the SOC where the system clock is turned off while RAM is
retained. This state would be entered when the kernel becomes idle for
extended periods and would have a high wake latency.  Resume would be
from the reset vector same as cold boot. The interface allows
restoration of states that were saved at the time of suspend.



:Symbol:           SYS_POWER_DEEP_SLEEP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Deep sleep state" if MICROKERNEL && SYS_POWER_MANAGEMENT && SYS_POWER_DEEP_SLEEP_SUPPORTED (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: MICROKERNEL && SYS_POWER_MANAGEMENT && SYS_POWER_DEEP_SLEEP_SUPPORTED (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SYS_POWER_MANAGEMENT (value: "n")
:Locations:
 * ../kernel/Kconfig:252