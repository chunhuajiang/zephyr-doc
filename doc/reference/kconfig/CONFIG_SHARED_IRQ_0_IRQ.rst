:orphan:

.. title:: SHARED_IRQ_0_IRQ

.. option:: CONFIG_SHARED_IRQ_0_IRQ:
.. _CONFIG_SHARED_IRQ_0_IRQ:

System interrupt number to be handled by this instance of the driver.



:Symbol:           SHARED_IRQ_0_IRQ
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "instance 0 interrupt" if SHARED_IRQ_0 (value: "n")
:Default values:

 *  18 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SHARED_IRQ && SOC_SERIES_QUARK_X1000 && SHARED_IRQ_0 (value: "n")
:Locations:
 * ../drivers/shared_irq/Kconfig:58
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:52