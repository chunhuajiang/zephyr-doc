:orphan:

.. title:: GPIO_ATMEL_SAM3_PORTD

.. option:: CONFIG_GPIO_ATMEL_SAM3_PORTD:
.. _CONFIG_GPIO_ATMEL_SAM3_PORTD:

Build the driver to utilize PIO controller Port D.



:Symbol:           GPIO_ATMEL_SAM3_PORTD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable driver for Atmel SAM3 PIO Port D" if GPIO_ATMEL_SAM3 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_ATMEL_SAM3 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.atmel_sam3:94
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:92