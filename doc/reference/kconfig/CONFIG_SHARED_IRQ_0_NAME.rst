:orphan:

.. title:: SHARED_IRQ_0_NAME

.. option:: CONFIG_SHARED_IRQ_0_NAME:
.. _CONFIG_SHARED_IRQ_0_NAME:

The configuration item CONFIG_SHARED_IRQ_0_NAME:

:Symbol:           SHARED_IRQ_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Select a name for the device" if SHARED_IRQ_0 (value: "n")
:Default values:

 *  "SHARED_IRQ0"
 *   Condition: SHARED_IRQ_0 (value: "n")
 *  "SHARED_IRQ0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SHARED_IRQ && SOC_SERIES_QUARK_X1000 && SHARED_IRQ_0 (value: "n")
:Locations:
 * ../drivers/shared_irq/Kconfig:53
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:50