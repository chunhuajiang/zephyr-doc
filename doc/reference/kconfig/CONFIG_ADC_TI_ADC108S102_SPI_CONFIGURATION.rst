:orphan:

.. title:: ADC_TI_ADC108S102_SPI_CONFIGURATION

.. option:: CONFIG_ADC_TI_ADC108S102_SPI_CONFIGURATION:
.. _CONFIG_ADC_TI_ADC108S102_SPI_CONFIGURATION:

Master SPI port configuration flags used to access adc108s102 chip.



:Symbol:           ADC_TI_ADC108S102_SPI_CONFIGURATION
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Master SPI port configuration" if ADC_TI_ADC108S102 (value: "n")
:Default values:

 *  0x0 (value: "n")
 *   Condition: ADC_TI_ADC108S102 (value: "n")
 *  0x81 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC && BOARD_GALILEO && ADC_TI_ADC108S102 (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:88
 * ../boards/x86/galileo/Kconfig.defconfig:40