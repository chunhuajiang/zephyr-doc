:orphan:

.. title:: SHARED_IRQ_0_PRI

.. option:: CONFIG_SHARED_IRQ_0_PRI:
.. _CONFIG_SHARED_IRQ_0_PRI:

Prioity of shared interrupt handler for the configured interrupt



:Symbol:           SHARED_IRQ_0_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "instance 0 interrupt priority" if SHARED_IRQ_0 (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: SHARED_IRQ_0 (value: "n")
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SHARED_IRQ && SOC_SERIES_QUARK_X1000 && SHARED_IRQ_0 (value: "n")
:Locations:
 * ../drivers/shared_irq/Kconfig:64
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:54