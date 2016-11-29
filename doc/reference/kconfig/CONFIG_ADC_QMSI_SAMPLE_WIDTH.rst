:orphan:

.. title:: ADC_QMSI_SAMPLE_WIDTH

.. option:: CONFIG_ADC_QMSI_SAMPLE_WIDTH:
.. _CONFIG_ADC_QMSI_SAMPLE_WIDTH:

Defines ADC device data sample width (resolution):

- 5 = 6 bits resolution

- 7 = 8 bits resolution

- 9 = 10 bits resolution

- 11 = 12 bits resolution


:Symbol:           ADC_QMSI_SAMPLE_WIDTH
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Sample Width"
 *  "Sample Width"
:Default values:

 *  3 (value: "n")
 *   Condition: (none)
 *  11 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC_QMSI_SS && (ADC_QMSI || ADC_QMSI_SS) (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:272
 * ../drivers/adc/Kconfig:288