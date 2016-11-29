:orphan:

.. title:: GPIO_QMSI_0

.. option:: CONFIG_GPIO_QMSI_0:
.. _CONFIG_GPIO_QMSI_0:

Include support for the GPIO port 0 using QMSI.



:Symbol:           GPIO_QMSI_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI GPIO block 0"
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
 GPIO && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:55
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:90
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:97
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:65