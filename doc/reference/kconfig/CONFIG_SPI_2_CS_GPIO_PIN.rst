:orphan:

.. title:: SPI_2_CS_GPIO_PIN

.. option:: CONFIG_SPI_2_CS_GPIO_PIN:
.. _CONFIG_SPI_2_CS_GPIO_PIN:

The configuration item CONFIG_SPI_2_CS_GPIO_PIN:

:Symbol:           SPI_2_CS_GPIO_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The GPIO PIN which is used to act as a CS pin" if SPI_2 && SPI_CS_GPIO (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SPI_2 && SPI_CS_GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:174