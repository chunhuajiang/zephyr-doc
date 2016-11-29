:orphan:

.. title:: ISL29035_GPIO_DEV_NAME

.. option:: CONFIG_ISL29035_GPIO_DEV_NAME:
.. _CONFIG_ISL29035_GPIO_DEV_NAME:

The device name of the GPIO device to which the ISL29035 interrupt
pin is connected.



:Symbol:           ISL29035_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if ISL29035 && ISL29035_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: ISL29035 && ISL29035_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:156