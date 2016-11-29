:orphan:

.. title:: TICKLESS_IDLE

.. option:: CONFIG_TICKLESS_IDLE:
.. _CONFIG_TICKLESS_IDLE:

This option suppresses periodic system clock interrupts whenever the
kernel becomes idle. This permits the system to remain in a power
saving state for extended periods without having to wake up to
service each tick as it occurs.

As a policy, an architecture should always provide support for tickless in
the microkernel. If an architecture also provides support for nanokernel
systems, it must select the NANOKERNEL_TICKLESS_IDLE_SUPPORTED kconfig
option.



:Symbol:           TICKLESS_IDLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Tickless idle"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SYS_POWER_MANAGEMENT (value: "n")
:Locations:
 * ../kernel/Kconfig:280