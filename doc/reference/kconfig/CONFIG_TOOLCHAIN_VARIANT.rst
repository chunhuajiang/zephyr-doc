:orphan:

.. title:: TOOLCHAIN_VARIANT

.. option:: CONFIG_TOOLCHAIN_VARIANT:
.. _CONFIG_TOOLCHAIN_VARIANT:

For optimized compilers with reduced features, specify the name
of the variant.



:Symbol:           TOOLCHAIN_VARIANT
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Cross-compiler variant name"
:Default values:

 *  "iamcu"
 *   Condition: X86_IAMCU (value: "n")
 *  ""
 *   Condition: !X86_IAMCU (value: "y")
 *  "iamcu"
 *   Condition: X86_IAMCU (value: "n")
 *  ""
 *   Condition: !X86_IAMCU (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../misc/Kconfig:92
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:25
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:25