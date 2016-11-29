:orphan:

.. title:: DHT_NAME

.. option:: CONFIG_DHT_NAME:
.. _CONFIG_DHT_NAME:

Device name with which the sensor is identified.



:Symbol:           DHT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver name" if DHT (value: "n")
:Default values:

 *  "DHT11"
 *   Condition: DHT_CHIP_DHT11 && DHT (value: "n")
 *  "DHT22"
 *   Condition: DHT_CHIP_DHT22 && DHT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/dht/Kconfig:48