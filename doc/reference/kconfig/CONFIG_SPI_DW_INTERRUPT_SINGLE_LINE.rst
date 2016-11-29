:orphan:

.. title:: SPI_DW_INTERRUPT_SINGLE_LINE

.. option:: CONFIG_SPI_DW_INTERRUPT_SINGLE_LINE:
.. _CONFIG_SPI_DW_INTERRUPT_SINGLE_LINE:

Only one line is used to trigger interrupts: RX, TX and ERROR
interrupt go all through that line, undifferentiated.


:Symbol:           SPI_DW_INTERRUPT_SINGLE_LINE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Single interrupt line for all interrupts"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI_DW && SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:44