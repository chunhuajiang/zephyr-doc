:orphan:

.. title:: AON_COUNTER_QMSI

.. option:: CONFIG_AON_COUNTER_QMSI:
.. _CONFIG_AON_COUNTER_QMSI:

Enable support for AON counter.



:Symbol:           AON_COUNTER_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "AON counter driver" if COUNTER && QMSI (value: "n")
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
 * ../drivers/counter/Kconfig:25
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:259
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:140
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:144