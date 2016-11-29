:orphan:

.. title:: GPIO_PCAL9535A_2_DEV_NAME

.. option:: CONFIG_GPIO_PCAL9535A_2_DEV_NAME:
.. _CONFIG_GPIO_PCAL9535A_2_DEV_NAME:

Specify the device name for the PCAL9535A I2C-based GPIO chip #2.



:Symbol:           GPIO_PCAL9535A_2_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #2 Device Name" if GPIO_PCAL9535A_2 (value: "n")
:Default values:

 *  "GPIO_P2"
 *   Condition: GPIO_PCAL9535A_2 (value: "n")
 *  "EXP2"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO && GPIO_PCAL9535A && GPIO_PCAL9535A_2 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:119
 * ../boards/x86/galileo/Kconfig.defconfig:89