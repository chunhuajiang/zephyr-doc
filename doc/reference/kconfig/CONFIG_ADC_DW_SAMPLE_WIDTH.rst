:orphan:

.. title:: ADC_DW_SAMPLE_WIDTH

.. option:: CONFIG_ADC_DW_SAMPLE_WIDTH:
.. _CONFIG_ADC_DW_SAMPLE_WIDTH:

Defines ADC device data sample width (resolution):

- 0 = 6 bits resolution

- 1 = 8 bits resolution

- 2 = 10 bits resolution

- 3 = 12 bits resolution



:Symbol:           ADC_DW_SAMPLE_WIDTH
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Sample Width" if ADC_DW (value: "n")
:Default values:

 *  31 (value: "n")
 *   Condition: ADC_DW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC_DW (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:187