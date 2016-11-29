:orphan:

.. title:: GPIO_DW_INIT_PRIORITY

.. option:: CONFIG_GPIO_DW_INIT_PRIORITY:
.. _CONFIG_GPIO_DW_INIT_PRIORITY:

Device driver initialization priority.



:Symbol:           GPIO_DW_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if GPIO_DW (value: "n")
:Default values:

 *  60 (value: "n")
 *   Condition: GPIO_DW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:34