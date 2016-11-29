:orphan:

.. title:: SOC_SERIES_QUARK_D2000

.. option:: CONFIG_SOC_SERIES_QUARK_D2000:
.. _CONFIG_SOC_SERIES_QUARK_D2000:

Enable support for Intel Quark D2000


:Symbol:           SOC_SERIES_QUARK_D2000
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark D2000 Series MCU"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_CPU_MINUTEIA`
 *  :option:`CONFIG_LOAPIC_TIMER`
 *  :option:`CONFIG_XIP`
 *  :option:`CONFIG_MVIC`
 *  :option:`CONFIG_HAS_QMSI`
 *  :option:`CONFIG_SOC_FAMILY_QUARK`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.series:16