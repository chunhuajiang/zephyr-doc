:orphan:

.. title:: ADC_QMSI_CALIBRATION

.. option:: CONFIG_ADC_QMSI_CALIBRATION:
.. _CONFIG_ADC_QMSI_CALIBRATION:

Enables ADC to run with a calibrated output at the
expense of execution speed when exiting low power states.
If disabled, the ADC will require the application/system-integrator
to provide a calibration method.



:Symbol:           ADC_QMSI_CALIBRATION
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Calibration"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC_QMSI || ADC_QMSI_SS (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:248