:orphan:

.. title:: SPI_2_CS_GPIO_PORT

.. option:: CONFIG_SPI_2_CS_GPIO_PORT:
.. _CONFIG_SPI_2_CS_GPIO_PORT:

The configuration item CONFIG_SPI_2_CS_GPIO_PORT:

:Symbol:           SPI_2_CS_GPIO_PORT
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO port which is used to control CS" if SPI_2 && SPI_CS_GPIO (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: SPI_2 && SPI_CS_GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:168