:orphan:

.. title:: GPIO_DW_0_CLOCK_GATE_SUBSYS

.. option:: CONFIG_GPIO_DW_0_CLOCK_GATE_SUBSYS:
.. _CONFIG_GPIO_DW_0_CLOCK_GATE_SUBSYS:

The configuration item CONFIG_GPIO_DW_0_CLOCK_GATE_SUBSYS:

:Symbol:           GPIO_DW_0_CLOCK_GATE_SUBSYS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Clock controller's subsystem" if GPIO_DW_CLOCK_GATE && GPIO_DW_0 (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:65