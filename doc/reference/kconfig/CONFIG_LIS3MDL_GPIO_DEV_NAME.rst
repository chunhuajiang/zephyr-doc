:orphan:

.. title:: LIS3MDL_GPIO_DEV_NAME

.. option:: CONFIG_LIS3MDL_GPIO_DEV_NAME:
.. _CONFIG_LIS3MDL_GPIO_DEV_NAME:

The device name of the GPIO device to which the LIS3MDL interrupt pins
are connected.



:Symbol:           LIS3MDL_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if LIS3MDL && LIS3MDL_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: LIS3MDL && LIS3MDL_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:81