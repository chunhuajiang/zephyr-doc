:orphan:

.. title:: ADC_DW_DUMMY_CONVERSION

.. option:: CONFIG_ADC_DW_DUMMY_CONVERSION:
.. _CONFIG_ADC_DW_DUMMY_CONVERSION:

After awaking from low power state a dummy
conversion must be performed and discarded.
If disabled the user will have to discard the first
sample after a resume from a low power state.



:Symbol:           ADC_DW_DUMMY_CONVERSION
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dummy conversion" if ADC_DW (value: "n")
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
 * ../drivers/adc/Kconfig:131