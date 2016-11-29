:orphan:

.. title:: GPIO_K64_C_DEV_NAME

.. option:: CONFIG_GPIO_K64_C_DEV_NAME:
.. _CONFIG_GPIO_K64_C_DEV_NAME:

Specify the device name.



:Symbol:           GPIO_K64_C_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based GPIO Port C Device Name" if GPIO_K64_C (value: "n")
:Default values:

 *  "GPIO_2"
 *   Condition: GPIO_K64_C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:83