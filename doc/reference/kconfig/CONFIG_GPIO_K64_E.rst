:orphan:

.. title:: GPIO_K64_E

.. option:: CONFIG_GPIO_K64_E:
.. _CONFIG_GPIO_K64_E:

Enable config options for Freescale K64-based GPIO port E.



:Symbol:           GPIO_K64_E
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based GPIO Port E" if GPIO_K64 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_K64 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:118
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:110
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:110