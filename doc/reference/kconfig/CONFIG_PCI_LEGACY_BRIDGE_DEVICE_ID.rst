:orphan:

.. title:: PCI_LEGACY_BRIDGE_DEVICE_ID

.. option:: CONFIG_PCI_LEGACY_BRIDGE_DEVICE_ID:
.. _CONFIG_PCI_LEGACY_BRIDGE_DEVICE_ID:

The configuration item CONFIG_PCI_LEGACY_BRIDGE_DEVICE_ID:

:Symbol:           PCI_LEGACY_BRIDGE_DEVICE_ID
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCI Legacy Bridge Device ID" if PCI_LEGACY_BRIDGE (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: PCI_LEGACY_BRIDGE (value: "n")
 *  0x095e (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PCI_LEGACY_BRIDGE && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/pci/Kconfig:63
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:69