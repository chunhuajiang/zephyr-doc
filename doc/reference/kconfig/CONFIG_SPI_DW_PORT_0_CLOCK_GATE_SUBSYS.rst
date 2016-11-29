:orphan:

.. title:: SPI_DW_PORT_0_CLOCK_GATE_SUBSYS

.. option:: CONFIG_SPI_DW_PORT_0_CLOCK_GATE_SUBSYS:
.. _CONFIG_SPI_DW_PORT_0_CLOCK_GATE_SUBSYS:

The configuration item CONFIG_SPI_DW_PORT_0_CLOCK_GATE_SUBSYS:

:Symbol:           SPI_DW_PORT_0_CLOCK_GATE_SUBSYS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Clock controller's subsystem" if SPI_DW_CLOCK_GATE (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI_DW && SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:73