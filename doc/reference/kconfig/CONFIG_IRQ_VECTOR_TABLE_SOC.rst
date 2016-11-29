:orphan:

.. title:: IRQ_VECTOR_TABLE_SOC

.. option:: CONFIG_IRQ_VECTOR_TABLE_SOC:
.. _CONFIG_IRQ_VECTOR_TABLE_SOC:

Not user-selectable, helps build system logic.



:Symbol:           IRQ_VECTOR_TABLE_SOC
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

 *  y (value: "y")
 *   Condition: SW_ISR_TABLE || !IRQ_VECTOR_TABLE_CUSTOM (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && (CPU_CORTEX_M0_M0PLUS || CPU_CORTEX_M3_M4 || CPU_CORTEX_M7) (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:237