:orphan:

.. title:: RTC_0_IRQ_PRI

.. option:: CONFIG_RTC_0_IRQ_PRI:
.. _CONFIG_RTC_0_IRQ_PRI:

RTC interrupt priority.



:Symbol:           RTC_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "RTC Driver Interrupt priority" if RTC (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 RTC && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/rtc/Kconfig:45
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:78
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:88
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:190