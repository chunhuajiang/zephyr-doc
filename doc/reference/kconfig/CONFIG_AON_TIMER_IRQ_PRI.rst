:orphan:

.. title:: AON_TIMER_IRQ_PRI

.. option:: CONFIG_AON_TIMER_IRQ_PRI:
.. _CONFIG_AON_TIMER_IRQ_PRI:

aon timer interrupt priority.



:Symbol:           AON_TIMER_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt priority" if AON_TIMER_QMSI (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 COUNTER && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/counter/Kconfig:55
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:265
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:144
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:148