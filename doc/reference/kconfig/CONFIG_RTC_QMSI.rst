:orphan:

.. title:: RTC_QMSI

.. option:: CONFIG_RTC_QMSI:
.. _CONFIG_RTC_QMSI:

Build QMSI RTC driver.



:Symbol:           RTC_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI RTC Driver" if QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 RTC && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/rtc/Kconfig:31
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:75
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:85
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:188