:orphan:

.. title:: PHYS_LOAD_ADDR

.. option:: CONFIG_PHYS_LOAD_ADDR:
.. _CONFIG_PHYS_LOAD_ADDR:

This option specifies the physical address where the kernel is loaded.



:Symbol:           PHYS_LOAD_ADDR
:Type:             hex
:Value:            "0x00100000"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Physical load address"
:Default values:

 *  0x00100000 (value: "n")
 *   Condition: (none)
 *  0x00180000 (value: "n")
 *   Condition: XIP (value: "n")
 *  0x00280000 (value: "n")
 *   Condition: !XIP (value: "y")
 *  0x40030000 (value: "n")
 *   Condition: XIP (value: "n")
 *  0x00100000 (value: "n")
 *   Condition: (none)
 *  0x00100000 (value: "n")
 *   Condition: (none)
 *  0x40010000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../arch/x86/core/Kconfig:63
 * ../arch/x86/soc/ia32/Kconfig.defconfig:24
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:32
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:32
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:25
 * ../arch/x86/soc/atom/Kconfig.defconfig:24
 * ../boards/x86/arduino_101/Kconfig.defconfig:16