:orphan:

.. title:: ADC_TI_ADC108S102_SPI_PORT_NAME

.. option:: CONFIG_ADC_TI_ADC108S102_SPI_PORT_NAME:
.. _CONFIG_ADC_TI_ADC108S102_SPI_PORT_NAME:

Master SPI port name through which adc108s102 chip is accessed.



:Symbol:           ADC_TI_ADC108S102_SPI_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Master SPI port name" if ADC_TI_ADC108S102 (value: "n")
:Default values:

 *  ""
 *   Condition: ADC_TI_ADC108S102 (value: "n")
 *  "SPI_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ADC && BOARD_GALILEO && ADC_TI_ADC108S102 (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:81
 * ../boards/x86/galileo/Kconfig.defconfig:38