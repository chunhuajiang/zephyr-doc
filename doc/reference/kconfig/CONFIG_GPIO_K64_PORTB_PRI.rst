:orphan:

.. title:: GPIO_K64_PORTB_PRI

.. option:: CONFIG_GPIO_K64_PORTB_PRI:
.. _CONFIG_GPIO_K64_PORTB_PRI:

K64 Port B IRQ priority



:Symbol:           GPIO_K64_PORTB_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based Port B interrupt priority" if GPIO_K64_B (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: GPIO_K64_B (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:69