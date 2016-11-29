:orphan:

.. title:: GPIO_DW_CLOCK_GATE

.. option:: CONFIG_GPIO_DW_CLOCK_GATE:
.. _CONFIG_GPIO_DW_CLOCK_GATE:

The configuration item CONFIG_GPIO_DW_CLOCK_GATE:

:Symbol:           GPIO_DW_CLOCK_GATE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable glock gating" if GPIO_DW (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_DW (value: "n")
:Selects:

 *  :option:`CONFIG_CLOCK_CONTROL` if GPIO_DW (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:42