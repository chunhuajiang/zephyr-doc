:orphan:

.. title:: PCI_LEGACY_BRIDGE_BUS

.. option:: CONFIG_PCI_LEGACY_BRIDGE_BUS:
.. _CONFIG_PCI_LEGACY_BRIDGE_BUS:

The configuration item CONFIG_PCI_LEGACY_BRIDGE_BUS:

:Symbol:           PCI_LEGACY_BRIDGE_BUS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCI Legacy Bridge Bus number" if PCI_LEGACY_BRIDGE (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: PCI_LEGACY_BRIDGE (value: "n")
 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PCI_LEGACY_BRIDGE && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/pci/Kconfig:48
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:63