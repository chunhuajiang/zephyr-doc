:orphan:

.. title:: GPIO_QMSI

.. option:: CONFIG_GPIO_QMSI:
.. _CONFIG_GPIO_QMSI:

Enable the GPIO driver found on Intel Microcontroller
boards, using the QMSI library.



:Symbol:           GPIO_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI GPIO driver" if GPIO && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && QMSI (value: "n")
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
 * ../drivers/gpio/Kconfig.qmsi:19
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:85
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:95
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:62