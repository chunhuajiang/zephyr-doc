:orphan:

.. title:: PCI_ENUMERATION

.. option:: CONFIG_PCI_ENUMERATION:
.. _CONFIG_PCI_ENUMERATION:

This option enables the PCI enumeration for device drivers.
This might be useful along with PCI_DEBUG to find out which
are the PCI settings of the devices. Once those are known and
statically set in every relevant driver's configuration, it
might be wise to disable this option to remove useless code.



:Symbol:           PCI_ENUMERATION
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable PCI device enumeration"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/pci/Kconfig:28
 * ../boards/x86/galileo/Kconfig.defconfig:28