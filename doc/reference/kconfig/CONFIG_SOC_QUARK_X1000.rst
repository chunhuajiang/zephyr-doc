:orphan:

.. title:: SOC_QUARK_X1000

.. option:: CONFIG_SOC_QUARK_X1000:
.. _CONFIG_SOC_QUARK_X1000:

Intel Quark X1000 SoC.


:Symbol:           SOC_QUARK_X1000
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark X1000" if SOC_SERIES_QUARK_X1000 (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_MINUTEIA` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_CPU_HAS_FPU` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_HPET_TIMER` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_BOOTLOADER_UNKNOWN` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_PCI` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED` if SOC_SERIES_QUARK_X1000 (value: "n")
 *  :option:`CONFIG_SYS_POWER_DEEP_SLEEP_SUPPORTED` if SOC_SERIES_QUARK_X1000 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.soc:2