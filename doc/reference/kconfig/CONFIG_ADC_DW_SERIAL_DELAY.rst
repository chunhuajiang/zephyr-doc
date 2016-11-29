:orphan:

.. title:: ADC_DW_SERIAL_DELAY

.. option:: CONFIG_ADC_DW_SERIAL_DELAY:
.. _CONFIG_ADC_DW_SERIAL_DELAY:

Number of ADC clock ticks that the first bit of
the serial output is delayed after the conversion
has started.



:Symbol:           ADC_DW_SERIAL_DELAY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Serial Delay"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC_DW (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:202