:orphan:

.. title:: PCI_LEGACY_BRIDGE

.. option:: CONFIG_PCI_LEGACY_BRIDGE:
.. _CONFIG_PCI_LEGACY_BRIDGE:

This option adds support for PCI legacy bridge device, that
allows direct setup of the PCI interrupt pin to IRQ number
mapping.



:Symbol:           PCI_LEGACY_BRIDGE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCI legacy bridge device support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PCI (value: "n")
:Locations:
 * ../drivers/pci/Kconfig:39