:orphan:

.. title:: ARCH_HAS_NANO_FIBER_ABORT

.. option:: CONFIG_ARCH_HAS_NANO_FIBER_ABORT:
.. _CONFIG_ARCH_HAS_NANO_FIBER_ABORT:

The configuration item CONFIG_ARCH_HAS_NANO_FIBER_ABORT:

:Symbol:           ARCH_HAS_NANO_FIBER_ABORT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && (CPU_CORTEX_M0_M0PLUS || CPU_CORTEX_M3_M4 || CPU_CORTEX_M7) (value: "n")
:Locations:
 * ../arch/arc/Kconfig:267
 * ../arch/arm/core/cortex_m/Kconfig:265