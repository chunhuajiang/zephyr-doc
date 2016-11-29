:orphan:

.. title:: AON_TIMER_QMSI

.. option:: CONFIG_AON_TIMER_QMSI:
.. _CONFIG_AON_TIMER_QMSI:

Enable support for AON periodic timer.



:Symbol:           AON_TIMER_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "AON periodic timer driver" if COUNTER && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: COUNTER && QMSI (value: "n")
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
 COUNTER && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/counter/Kconfig:40
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:262
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:142
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:146