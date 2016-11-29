:orphan:

.. title:: ARC_GDB_ENABLE

.. option:: CONFIG_ARC_GDB_ENABLE:
.. _CONFIG_ARC_GDB_ENABLE:

This option will stop the master processor from boot-strapping
the ARC slave processor. This will allow GDB to halt and
engage the ARC processor to proceed step by step execution.



:Symbol:           ARC_GDB_ENABLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Allows the usage of GDB with the ARC processor." if ARC_INIT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ARC_INIT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:61