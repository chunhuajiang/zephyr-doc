:orphan:

.. title:: DHT_GPIO_DEV_NAME

.. option:: CONFIG_DHT_GPIO_DEV_NAME:
.. _CONFIG_DHT_GPIO_DEV_NAME:

The device name of the GPIO device to which the chip's data pin
is connected.



:Symbol:           DHT_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if DHT (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: DHT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/dht/Kconfig:57