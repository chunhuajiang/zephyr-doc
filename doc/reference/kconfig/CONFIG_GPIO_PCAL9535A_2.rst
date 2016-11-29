:orphan:

.. title:: GPIO_PCAL9535A_2

.. option:: CONFIG_GPIO_PCAL9535A_2:
.. _CONFIG_GPIO_PCAL9535A_2:

Enable config options for the PCAL9535A I2C-based GPIO chip #2.



:Symbol:           GPIO_PCAL9535A_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #2" if GPIO_PCAL9535A (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_PCAL9535A (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO && GPIO_PCAL9535A (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:112
 * ../boards/x86/galileo/Kconfig.defconfig:84