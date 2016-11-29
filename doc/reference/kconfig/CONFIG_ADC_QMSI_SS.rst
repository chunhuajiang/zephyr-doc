:orphan:

.. title:: ADC_QMSI_SS

.. option:: CONFIG_ADC_QMSI_SS:
.. _CONFIG_ADC_QMSI_SS:

Enable the driver implementation of the QMSI ADC IP.



:Symbol:           ADC_QMSI_SS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI ADC Driver for the Sensor Subsystem" if QMSI && ADC (value: "n")
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
 ADC && SOC_QUARK_SE_C1000_SS (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:225
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:181