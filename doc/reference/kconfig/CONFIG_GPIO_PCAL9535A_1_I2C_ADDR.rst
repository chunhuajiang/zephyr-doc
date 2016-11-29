:orphan:

.. title:: GPIO_PCAL9535A_1_I2C_ADDR

.. option:: CONFIG_GPIO_PCAL9535A_1_I2C_ADDR:
.. _CONFIG_GPIO_PCAL9535A_1_I2C_ADDR:

Specify the I2C slave address for the PCAL9535A I2C-based GPIO chip #1.



:Symbol:           GPIO_PCAL9535A_1_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #1 I2C slave address" if GPIO_PCAL9535A_1 (value: "n")
:Default values:

 *  0x26 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && I2C && BOARD_GALILEO && GPIO_PCAL9535A && GPIO_PCAL9535A_1 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:98
 * ../boards/x86/galileo/Kconfig.defconfig:77