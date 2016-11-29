:orphan:

.. title:: LIS3DH_GPIO_DEV_NAME

.. option:: CONFIG_LIS3DH_GPIO_DEV_NAME:
.. _CONFIG_LIS3DH_GPIO_DEV_NAME:

The device name of the GPIO device to which the LIS3DH interrupt pins
are connected.



:Symbol:           LIS3DH_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if LIS3DH && LIS3DH_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: LIS3DH && LIS3DH_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3dh/Kconfig:84