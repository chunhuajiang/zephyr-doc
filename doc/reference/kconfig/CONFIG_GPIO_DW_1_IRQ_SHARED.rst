:orphan:

.. title:: GPIO_DW_1_IRQ_SHARED

.. option:: CONFIG_GPIO_DW_1_IRQ_SHARED:
.. _CONFIG_GPIO_DW_1_IRQ_SHARED:

When interrupts fire, the shared IRQ driver is notified. Then the shared IRQ
driver dispatches the interrupt to other drivers.



:Symbol:           GPIO_DW_1_IRQ_SHARED
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
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:129