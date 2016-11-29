:orphan:

.. title:: SOC_SERIES_QUARK_SE

.. option:: CONFIG_SOC_SERIES_QUARK_SE:
.. _CONFIG_SOC_SERIES_QUARK_SE:

Enable support for Quark SE


:Symbol:           SOC_SERIES_QUARK_SE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE Series MCU"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_SOC_FAMILY_QUARK`
 *  :option:`CONFIG_CPU_MINUTEIA`
 *  :option:`CONFIG_IOAPIC`
 *  :option:`CONFIG_LOAPIC`
 *  :option:`CONFIG_LOAPIC_TIMER`
 *  :option:`CONFIG_XIP`
 *  :option:`CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED`
 *  :option:`CONFIG_SYS_POWER_DEEP_SLEEP_SUPPORTED`
 *  :option:`CONFIG_BOOTLOADER_CONTEXT_RESTORE_SUPPORTED`
 *  :option:`CONFIG_HAS_QMSI`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.series:16