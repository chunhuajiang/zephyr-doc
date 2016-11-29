:orphan:

.. title:: GROVE_TEMPERATURE_SENSOR

.. option:: CONFIG_GROVE_TEMPERATURE_SENSOR:
.. _CONFIG_GROVE_TEMPERATURE_SENSOR:

Setting this value will enable dirver support for the Grove
Temperature Sensor.



:Symbol:           GROVE_TEMPERATURE_SENSOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable the Seeed Grove Temperature Sensor" if SENSOR && GROVE && ADC && NEWLIB_LIBC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && GROVE && ADC && NEWLIB_LIBC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/grove/Kconfig:95