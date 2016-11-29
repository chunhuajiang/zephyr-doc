:orphan:

.. title:: DMA_QMSI

.. option:: CONFIG_DMA_QMSI:
.. _CONFIG_DMA_QMSI:

QMSI DMA driver.



:Symbol:           DMA_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable QMSI DMA driver" if QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 DMA && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/dma/Kconfig:28
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:252
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:154
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:231