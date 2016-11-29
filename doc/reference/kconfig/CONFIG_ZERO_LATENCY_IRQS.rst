:orphan:

.. title:: ZERO_LATENCY_IRQS

.. option:: CONFIG_ZERO_LATENCY_IRQS:
.. _CONFIG_ZERO_LATENCY_IRQS:

Interrupt locking is done by setting exception masking to priority
one, thus allowing exception of priority zero to still come in. By
default, the kernel verifies, via __ASSERT() statements, that the
interrupt priority is not set to zero when either connecting them or
setting their priority. Enabling this option disables the check,
thus allowing setting the priority of interrupts to zero.

Note that this is a somewhat dangerous option: ISRs of priority zero
interrupts cannot use any kernel functionality.



:Symbol:           ZERO_LATENCY_IRQS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable zero-latency interrupts"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && (CPU_CORTEX_M0_M0PLUS || CPU_CORTEX_M3_M4 || CPU_CORTEX_M7) (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:245