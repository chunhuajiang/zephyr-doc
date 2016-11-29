:orphan:

.. title:: GPIO_PCAL9535A_3_DEV_NAME

.. option:: CONFIG_GPIO_PCAL9535A_3_DEV_NAME:
.. _CONFIG_GPIO_PCAL9535A_3_DEV_NAME:

Specify the device name for the PCAL9535A I2C-based GPIO chip #3.



:Symbol:           GPIO_PCAL9535A_3_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCAL9535A GPIO chip #3 Device Name" if GPIO_PCAL9535A_3 (value: "n")
:Default values:

 *  "GPIO_P3"
 *   Condition: GPIO_PCAL9535A_3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_PCAL9535A && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.pcal9535a:147