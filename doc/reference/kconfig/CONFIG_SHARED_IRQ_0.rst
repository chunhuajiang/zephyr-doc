:orphan:

.. title:: SHARED_IRQ_0

.. option:: CONFIG_SHARED_IRQ_0:
.. _CONFIG_SHARED_IRQ_0:

Provide an instance of the shared interrupt driver when system
configuration requires that multiple devices share an interrupt.



:Symbol:           SHARED_IRQ_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared interrupt instance 0" if SHARED_IRQ (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SHARED_IRQ && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/shared_irq/Kconfig:46
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:45