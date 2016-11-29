:orphan:

.. title:: X86_IAMCU

.. option:: CONFIG_X86_IAMCU:
.. _CONFIG_X86_IAMCU:

The IAMCU calling convention changes the X86 C calling convention to
pass some arguments via registers allowing for code size and performance
improvements.  Great care needs to be taken if you have assembly code
that will be called from C or C code called from assembly code, the
assembly code will need to be updated to conform to the new calling
convention.  If in doubt say N



:Symbol:           X86_IAMCU
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IAMCU calling convention"
:Default values:

 *  n (value: "n")
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
 SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../arch/x86/Kconfig:71
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:22
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:22