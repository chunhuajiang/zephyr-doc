:orphan:

.. title:: PHYS_RAM_ADDR

.. option:: CONFIG_PHYS_RAM_ADDR:
.. _CONFIG_PHYS_RAM_ADDR:

This option specifies the physical SRAM address of this Soc.



:Symbol:           PHYS_RAM_ADDR
:Type:             hex
:Value:            "0x00400000"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Physical RAM address"
:Default values:

 *  0x00400000 (value: "n")
 *   Condition: (none)
 *  0x00280000 (value: "n")
 *   Condition: (none)
 *  0xA8006400 (value: "n")
 *   Condition: (none)
 *  0x00400000 (value: "n")
 *   Condition: (none)
 *  0x00400000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_ATOM (value: "n")
:Locations:
 * ../arch/x86/core/Kconfig:69
 * ../arch/x86/soc/ia32/Kconfig.defconfig:27
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:54
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:29
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:28
 * ../arch/x86/soc/atom/Kconfig.defconfig:27