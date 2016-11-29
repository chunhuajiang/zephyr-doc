:orphan:

.. title:: ROM_SIZE

.. option:: CONFIG_ROM_SIZE:
.. _CONFIG_ROM_SIZE:

This option specifies the amount of ROM given to the kernel. It must
not exceed the amount available on the target.  It must also be large
enough to contain the full image.

The default value is specified by the board.



:Symbol:           ROM_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Amount of ROM given to the kernel (in kB)" if XIP (value: "n")
:Default values:

 *  72 (value: "n")
 *   Condition: XIP (value: "n")
 *  32 (value: "n")
 *   Condition: (none)
 *  144 (value: "n")
 *   Condition: (none)
 *  1024 (value: "n")
 *   Condition: XIP (value: "n")
 *  72 (value: "n")
 *   Condition: XIP (value: "n")
 *  192 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../arch/x86/core/Kconfig:86
 * ../arch/x86/soc/ia32/Kconfig.defconfig:34
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:39
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:38
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:34
 * ../arch/x86/soc/atom/Kconfig.defconfig:34
 * ../boards/x86/arduino_101/Kconfig.defconfig:13