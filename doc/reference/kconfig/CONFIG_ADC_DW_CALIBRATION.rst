:orphan:

.. title:: ADC_DW_CALIBRATION

.. option:: CONFIG_ADC_DW_CALIBRATION:
.. _CONFIG_ADC_DW_CALIBRATION:

Enables ADC to run with a calibrated output at the
expense of execution speed when exiting low power states.
If disabled, the ADC will require the application/system-integrator
to provide a calibration method.



:Symbol:           ADC_DW_CALIBRATION
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Calibration" if ADC_DW (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: ADC_DW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC_DW (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:121