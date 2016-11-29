:orphan:

.. title:: GPIO_ATMEL_SAM3

.. option:: CONFIG_GPIO_ATMEL_SAM3:
.. _CONFIG_GPIO_ATMEL_SAM3:

Enable config options to support the PIO controllers
on Atmel SAM3 family processors.

Says n if not sure.



:Symbol:           GPIO_ATMEL_SAM3
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 PIO Controllers" if GPIO && SOC_ATMEL_SAM3 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && SOC_ATMEL_SAM3 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.atmel_sam3:19
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:80