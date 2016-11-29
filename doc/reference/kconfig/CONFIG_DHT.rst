:orphan:

.. title:: DHT

.. option:: CONFIG_DHT:
.. _CONFIG_DHT:

Enable driver for the DHT temperature and humidity sensor family.



:Symbol:           DHT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DHT Temperature and Humidity Sensor" if SENSOR && GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/dht/Kconfig:19