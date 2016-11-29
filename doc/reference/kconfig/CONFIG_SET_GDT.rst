:orphan:

.. title:: SET_GDT

.. option:: CONFIG_SET_GDT:
.. _CONFIG_SET_GDT:

This option sets up the GDT as part of the boot process. However,
this may conflict with some security scenarios where the GDT is
already appropriately set by an earlier bootloader stage, in which
case this should be disabled. If disabled, the global _gdt pointer
will not be available.



:Symbol:           SET_GDT
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Setup GDT as part of boot process"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:95