:orphan:

.. title:: GPIO_NRF5_P0_DEV_NAME

.. option:: CONFIG_GPIO_NRF5_P0_DEV_NAME:
.. _CONFIG_GPIO_NRF5_P0_DEV_NAME:

Specify the device name to be used for the GPIO port.



:Symbol:           GPIO_NRF5_P0_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO Port P0 Device Name" if GPIO_NRF5_P0 (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: GPIO_NRF5_P0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_NRF5 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.nrf5:34