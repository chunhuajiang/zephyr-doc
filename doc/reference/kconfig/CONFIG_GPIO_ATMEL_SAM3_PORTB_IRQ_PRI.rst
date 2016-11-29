:orphan:

.. title:: GPIO_ATMEL_SAM3_PORTB_IRQ_PRI

.. option:: CONFIG_GPIO_ATMEL_SAM3_PORTB_IRQ_PRI:
.. _CONFIG_GPIO_ATMEL_SAM3_PORTB_IRQ_PRI:

Interrupt priority for Port B.



:Symbol:           GPIO_ATMEL_SAM3_PORTB_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt Priority for Port B" if GPIO_ATMEL_SAM3_PORTB (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: GPIO_ATMEL_SAM3_PORTB (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_ATMEL_SAM3 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.atmel_sam3:66