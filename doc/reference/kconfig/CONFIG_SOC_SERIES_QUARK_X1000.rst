:orphan:

.. title:: SOC_SERIES_QUARK_X1000

.. option:: CONFIG_SOC_SERIES_QUARK_X1000:
.. _CONFIG_SOC_SERIES_QUARK_X1000:

Intel Quark X1000 SoC.


:Symbol:           SOC_SERIES_QUARK_X1000
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Intel Quark X1000 Series"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_MINUTEIA`
 *  :option:`CONFIG_CPU_HAS_FPU`
 *  :option:`CONFIG_HPET_TIMER`
 *  :option:`CONFIG_BOOTLOADER_UNKNOWN`
 *  :option:`CONFIG_PCI`
 *  :option:`CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED`
 *  :option:`CONFIG_SYS_POWER_DEEP_SLEEP_SUPPORTED`
 *  :option:`CONFIG_SOC_FAMILY_QUARK`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.series:2