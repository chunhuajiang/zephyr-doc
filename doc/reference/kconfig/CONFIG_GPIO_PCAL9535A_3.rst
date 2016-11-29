:orphan:

.. title:: GPIO_PCAL9535A_3

.. option:: CONFIG_GPIO_PCAL9535A_3:
.. _CONFIG_GPIO_PCAL9535A_3:

Enable config options for the PCAL9535A I2C-based GPIO chip #3.



:Symbol:           GPIO_PCAL9535A_3
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #3" if GPIO_PCAL9535A (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_PCAL9535A (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_PCAL9535A && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:140