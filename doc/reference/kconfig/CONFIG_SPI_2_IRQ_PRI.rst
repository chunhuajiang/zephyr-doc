:orphan:

.. title:: SPI_2_IRQ_PRI

.. option:: CONFIG_SPI_2_IRQ_PRI:
.. _CONFIG_SPI_2_IRQ_PRI:

The configuration item CONFIG_SPI_2_IRQ_PRI:

:Symbol:           SPI_2_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 2 interrupt priority" if SPI_2 (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:163
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:169
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:169