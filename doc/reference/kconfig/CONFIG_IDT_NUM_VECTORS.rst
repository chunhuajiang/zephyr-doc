:orphan:

.. title:: IDT_NUM_VECTORS

.. option:: CONFIG_IDT_NUM_VECTORS:
.. _CONFIG_IDT_NUM_VECTORS:

This option specifies the number of interrupt vector entries in the
Interrupt Descriptor Table (IDT). By default all 256 vectors are
supported in an IDT requiring 2048 bytes of memory.



:Symbol:           IDT_NUM_VECTORS
:Type:             int
:Value:            "256"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [32, 256]
:Prompts:

 *  "Number of IDT vectors"
:Default values:

 *  256 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_QUARK_D2000 (value: "n")
:Locations:
 * ../arch/x86/core/Kconfig:41
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:42