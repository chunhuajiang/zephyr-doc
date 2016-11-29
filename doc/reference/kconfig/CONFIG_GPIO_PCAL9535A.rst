:orphan:

.. title:: GPIO_PCAL9535A

.. option:: CONFIG_GPIO_PCAL9535A:
.. _CONFIG_GPIO_PCAL9535A:

Enable driver for PCAL9535A I2C-based GPIO chip.



:Symbol:           GPIO_PCAL9535A
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A I2C-based GPIO chip" if GPIO && I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && I2C (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_NANO_TIMERS` if GPIO && I2C (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:19
 * ../boards/x86/galileo/Kconfig.defconfig:51