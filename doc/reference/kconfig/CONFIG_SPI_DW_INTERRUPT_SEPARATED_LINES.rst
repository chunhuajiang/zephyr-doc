:orphan:

.. title:: SPI_DW_INTERRUPT_SEPARATED_LINES

.. option:: CONFIG_SPI_DW_INTERRUPT_SEPARATED_LINES:
.. _CONFIG_SPI_DW_INTERRUPT_SEPARATED_LINES:

Each interrupt gets a dedicated line


:Symbol:           SPI_DW_INTERRUPT_SEPARATED_LINES
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "One line per-interrupt type (RX, TX and ERROR)"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI_DW && SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:49