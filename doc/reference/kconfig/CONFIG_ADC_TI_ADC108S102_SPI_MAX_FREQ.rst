:orphan:

.. title:: ADC_TI_ADC108S102_SPI_MAX_FREQ

.. option:: CONFIG_ADC_TI_ADC108S102_SPI_MAX_FREQ:
.. _CONFIG_ADC_TI_ADC108S102_SPI_MAX_FREQ:

Master SPI port maximum frequency used to access adc108s102 chip.



:Symbol:           ADC_TI_ADC108S102_SPI_MAX_FREQ
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Master SPI port max frequency" if ADC_TI_ADC108S102 (value: "n")
:Default values:

 *  0x0 (value: "n")
 *   Condition: ADC_TI_ADC108S102 (value: "n")
 *  0x20000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC && BOARD_GALILEO && ADC_TI_ADC108S102 (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:95
 * ../boards/x86/galileo/Kconfig.defconfig:42