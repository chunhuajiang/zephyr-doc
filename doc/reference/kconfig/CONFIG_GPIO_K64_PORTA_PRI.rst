:orphan:

.. title:: GPIO_K64_PORTA_PRI

.. option:: CONFIG_GPIO_K64_PORTA_PRI:
.. _CONFIG_GPIO_K64_PORTA_PRI:

K64 Port A IRQ priority



:Symbol:           GPIO_K64_PORTA_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based Port A interrupt priority" if GPIO_K64_A (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: GPIO_K64_A (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:48