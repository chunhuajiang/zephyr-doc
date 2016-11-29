:orphan:

.. title:: GPIO_ATMEL_SAM3_PORTC_DEV_NAME

.. option:: CONFIG_GPIO_ATMEL_SAM3_PORTC_DEV_NAME:
.. _CONFIG_GPIO_ATMEL_SAM3_PORTC_DEV_NAME:

Device name for Port C.



:Symbol:           GPIO_ATMEL_SAM3_PORTC_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Port C" if GPIO_ATMEL_SAM3_PORTC (value: "n")
:Default values:

 *  "PIOC"
 *   Condition: GPIO_ATMEL_SAM3_PORTC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_ATMEL_SAM3 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.atmel_sam3:80