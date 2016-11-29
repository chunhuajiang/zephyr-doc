:orphan:

.. title:: GPIO_K64_PORTC_PRI

.. option:: CONFIG_GPIO_K64_PORTC_PRI:
.. _CONFIG_GPIO_K64_PORTC_PRI:

K64 Port C IRQ priority



:Symbol:           GPIO_K64_PORTC_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based Port C interrupt priority" if GPIO_K64_C (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: GPIO_K64_C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:90