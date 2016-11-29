:orphan:

.. title:: SPI_2

.. option:: CONFIG_SPI_2:
.. _CONFIG_SPI_2:

Enable SPI controller port 2.



:Symbol:           SPI_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SPI port 2"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:150
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:166
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:166