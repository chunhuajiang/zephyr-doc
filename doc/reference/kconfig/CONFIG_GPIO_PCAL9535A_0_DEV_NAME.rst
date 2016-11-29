:orphan:

.. title:: GPIO_PCAL9535A_0_DEV_NAME

.. option:: CONFIG_GPIO_PCAL9535A_0_DEV_NAME:
.. _CONFIG_GPIO_PCAL9535A_0_DEV_NAME:

Specify the device name for the PCAL9535A I2C-based GPIO chip #0.



:Symbol:           GPIO_PCAL9535A_0_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #0 Device Name" if GPIO_PCAL9535A_0 (value: "n")
:Default values:

 *  "GPIO_P0"
 *   Condition: GPIO_PCAL9535A_0 (value: "n")
 *  "EXP0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO && GPIO_PCAL9535A && GPIO_PCAL9535A_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:63
 * ../boards/x86/galileo/Kconfig.defconfig:61