:orphan:

.. title:: GPIO_K64_C

.. option:: CONFIG_GPIO_K64_C:
.. _CONFIG_GPIO_K64_C:

Enable config options for Freescale K64-based GPIO port C.



:Symbol:           GPIO_K64_C
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based GPIO Port B" if GPIO_K64 (value: "n")
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
 * ../drivers/gpio/Kconfig.k64:76
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:104
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:104