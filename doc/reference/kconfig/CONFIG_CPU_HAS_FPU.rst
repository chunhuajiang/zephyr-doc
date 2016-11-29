:orphan:

.. title:: CPU_HAS_FPU

.. option:: CONFIG_CPU_HAS_FPU:
.. _CONFIG_CPU_HAS_FPU:

This option is enabled when the CPU has a hardware floating point
unit.



:Symbol:           CPU_HAS_FPU
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: !X86_IAMCU (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_SERIES_QUARK_X1000 || CPU_ATOM && X86 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 || SOC_MK64F12 && ARM || SOC_NRF52832 && ARM (value: "n")
:Additional dependencies from enclosing menus and ifs:
 BOARD_QEMU_X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:61
 * ../arch/arm/core/Kconfig:35
 * ../boards/x86/qemu_x86/Kconfig.defconfig:7