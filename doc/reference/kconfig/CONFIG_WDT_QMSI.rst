:orphan:

.. title:: WDT_QMSI

.. option:: CONFIG_WDT_QMSI:
.. _CONFIG_WDT_QMSI:

This option enables the QMSI watchdog driver.

This driver is simply a shim driver based on the watchdog
driver provided by the QMSI BSP.



:Symbol:           WDT_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI Watchdog driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
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
 WATCHDOG && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig:30
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:242
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:77
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:180