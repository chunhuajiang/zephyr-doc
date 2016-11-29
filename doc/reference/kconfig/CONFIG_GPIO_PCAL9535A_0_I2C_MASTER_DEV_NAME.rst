:orphan:

.. title:: GPIO_PCAL9535A_0_I2C_MASTER_DEV_NAME

.. option:: CONFIG_GPIO_PCAL9535A_0_I2C_MASTER_DEV_NAME:
.. _CONFIG_GPIO_PCAL9535A_0_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which this
PCAL9535A chip #0 is binded.



:Symbol:           GPIO_PCAL9535A_0_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master where PCAL9535A GPIO chip #0 is connected" if GPIO_PCAL9535A_0 (value: "n")
:Default values:

 *  ""
 *   Condition: GPIO_PCAL9535A_0 (value: "n")
 *  I2C_0_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO && GPIO_PCAL9535A && GPIO_PCAL9535A_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:76
 * ../boards/x86/galileo/Kconfig.defconfig:65