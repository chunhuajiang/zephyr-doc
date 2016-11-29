:orphan:

.. title:: HTS221_GPIO_DEV_NAME

.. option:: CONFIG_HTS221_GPIO_DEV_NAME:
.. _CONFIG_HTS221_GPIO_DEV_NAME:

The device name of the GPIO device to which the HTS221 interrupt pin
is connected.



:Symbol:           HTS221_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if HTS221 && HTS221_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: HTS221 && HTS221_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:71