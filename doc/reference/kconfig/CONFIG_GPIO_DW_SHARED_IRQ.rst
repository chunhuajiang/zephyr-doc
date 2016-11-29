:orphan:

.. title:: GPIO_DW_SHARED_IRQ

.. option:: CONFIG_GPIO_DW_SHARED_IRQ:
.. _CONFIG_GPIO_DW_SHARED_IRQ:

The configuration item CONFIG_GPIO_DW_SHARED_IRQ:

:Symbol:           GPIO_DW_SHARED_IRQ
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_DW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GPIO_DW && GPIO && SHARED_IRQ && GPIO_DW_0_IRQ_SHARED || GPIO_DW && GPIO && SHARED_IRQ && GPIO_DW_1_IRQ_SHARED || GPIO_DW && GPIO && SHARED_IRQ && GPIO_DW_2_IRQ_SHARED || GPIO_DW && GPIO && SHARED_IRQ && GPIO_DW_3_IRQ_SHARED (value: "n")
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:29