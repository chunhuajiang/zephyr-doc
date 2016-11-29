:orphan:

.. title:: RAM_SIZE

.. option:: CONFIG_RAM_SIZE:
.. _CONFIG_RAM_SIZE:

This option specifies the amount of RAM given to the kernel. It must
not exceed the amount available on the target.  When running an XIP
kernel, it must be large enough to contain the data, bss and noinit
sections.  When not running an XIP kernel, it must be large enough to
contain the full image.

The default value is specified by the board.



:Symbol:           RAM_SIZE
:Type:             int
:Value:            "192"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Amount of RAM given to the kernel (in kB)"
:Default values:

 *  128 (value: "n")
 *   Condition: XIP (value: "n")
 *  192 (value: "n")
 *   Condition: (none)
 *  8 (value: "n")
 *   Condition: (none)
 *  55 (value: "n")
 *   Condition: (none)
 *  32768 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: XIP (value: "n")
 *  192 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_ATOM (value: "n")
:Locations:
 * ../arch/x86/core/Kconfig:75
 * ../arch/x86/soc/ia32/Kconfig.defconfig:30
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:36
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:35
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:31
 * ../arch/x86/soc/atom/Kconfig.defconfig:30