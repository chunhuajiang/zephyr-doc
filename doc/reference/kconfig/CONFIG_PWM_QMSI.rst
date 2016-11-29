:orphan:

.. title:: PWM_QMSI

.. option:: CONFIG_PWM_QMSI:
.. _CONFIG_PWM_QMSI:

Enable QMSI PWM driver. This driver will use the QMSI library to
access the SOC underlying timer IP block. This driver uses the
DesignWare IP block that can be also handled by the PWM_DW driver



:Symbol:           PWM_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI PWM Driver" if QMSI && PWM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI && PWM (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.qmsi:19
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:105
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:57