:orphan:

.. title:: SW_ISR_TABLE

.. option:: CONFIG_SW_ISR_TABLE:
.. _CONFIG_SW_ISR_TABLE:

Enable an interrupt handler table implemented in software. This
table, unlike ISRs connected directly in the vector table, allow
a parameter to be passed to the interrupt handlers. Also, invoking
the exeception/interrupt exit stub is automatically done.



:Symbol:           SW_ISR_TABLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable software interrupt handler table"
 *  "Enable software interrupt handler table"
:Default values:

 *  y (value: "y")
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
 * ../arch/arc/Kconfig:222
 * ../arch/arm/core/cortex_m/Kconfig:205