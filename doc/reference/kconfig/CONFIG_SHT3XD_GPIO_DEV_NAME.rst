:orphan:

.. title:: SHT3XD_GPIO_DEV_NAME

.. option:: CONFIG_SHT3XD_GPIO_DEV_NAME:
.. _CONFIG_SHT3XD_GPIO_DEV_NAME:

The device name of the GPIO device to which the SHT3xD interrupt
pins are connected.



:Symbol:           SHT3XD_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if SHT3XD && SHT3XD_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: SHT3XD && SHT3XD_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:83