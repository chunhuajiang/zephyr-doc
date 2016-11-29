:orphan:

.. title:: GPIO_DW_0_IRQ_SHARED

.. option:: CONFIG_GPIO_DW_0_IRQ_SHARED:
.. _CONFIG_GPIO_DW_0_IRQ_SHARED:

When interrupts fire, the shared IRQ driver is notified. Then the shared IRQ
driver dispatches the interrupt to other drivers.



:Symbol:           GPIO_DW_0_IRQ_SHARED
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared IRQ" if SHARED_IRQ (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_GPIO_DW_SHARED_IRQ` if SHARED_IRQ (value: "n")
:Reverse (select-related) dependencies:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_DW && SHARED_IRQ && GPIO_DW_0 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:79