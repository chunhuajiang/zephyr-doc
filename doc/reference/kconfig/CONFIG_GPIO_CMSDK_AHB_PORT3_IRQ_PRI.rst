:orphan:

.. title:: GPIO_CMSDK_AHB_PORT3_IRQ_PRI

.. option:: CONFIG_GPIO_CMSDK_AHB_PORT3_IRQ_PRI:
.. _CONFIG_GPIO_CMSDK_AHB_PORT3_IRQ_PRI:

Interrupt priority for Port 3.



:Symbol:           GPIO_CMSDK_AHB_PORT3_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt Priority for Port 3" if GPIO_CMSDK_AHB_PORT3 (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: GPIO_CMSDK_AHB_PORT3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_CMSDK_AHB && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.cmsdk_ahb:115