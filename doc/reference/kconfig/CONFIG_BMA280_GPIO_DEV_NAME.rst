:orphan:

.. title:: BMA280_GPIO_DEV_NAME

.. option:: CONFIG_BMA280_GPIO_DEV_NAME:
.. _CONFIG_BMA280_GPIO_DEV_NAME:

The device name of the GPIO device to which the chip's interrupt pins
are connected.



:Symbol:           BMA280_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if BMA280 && BMA280_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: BMA280 && BMA280_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bma280/Kconfig:109