:orphan:

.. title:: GPIO_PCAL9535A_3_I2C_MASTER_DEV_NAME

.. option:: CONFIG_GPIO_PCAL9535A_3_I2C_MASTER_DEV_NAME:
.. _CONFIG_GPIO_PCAL9535A_3_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which this
PCAL9535A chip #3 is binded.



:Symbol:           GPIO_PCAL9535A_3_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master where PCAL9535A GPIO chip #3 is connected" if GPIO_PCAL9535A_3 (value: "n")
:Default values:

 *  ""
 *   Condition: GPIO_PCAL9535A_3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_PCAL9535A && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:160