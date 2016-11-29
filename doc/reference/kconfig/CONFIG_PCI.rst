:orphan:

.. title:: PCI

.. option:: CONFIG_PCI:
.. _CONFIG_PCI:

This options enables support of PCI bus for device drivers.



:Symbol:           PCI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCI Settings" if X86 (value: "y")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_X1000 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/pci/Kconfig:20