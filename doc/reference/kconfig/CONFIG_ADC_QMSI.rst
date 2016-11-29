:orphan:

.. title:: ADC_QMSI

.. option:: CONFIG_ADC_QMSI:
.. _CONFIG_ADC_QMSI:

Enable the driver implementation of the QMSI ADC IP.



:Symbol:           ADC_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI ADC Driver" if QMSI && ADC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI && ADC (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC && SOC_SERIES_QUARK_D2000 (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:218
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:149