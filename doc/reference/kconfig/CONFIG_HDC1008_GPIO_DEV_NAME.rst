:orphan:

.. title:: HDC1008_GPIO_DEV_NAME

.. option:: CONFIG_HDC1008_GPIO_DEV_NAME:
.. _CONFIG_HDC1008_GPIO_DEV_NAME:

The device name of the GPIO device to which the HDC1008 data-ready
pin is connected.



:Symbol:           HDC1008_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if HDC1008 (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: HDC1008 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hdc1008/Kconfig:55