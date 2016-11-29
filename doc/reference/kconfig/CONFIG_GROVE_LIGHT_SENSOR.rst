:orphan:

.. title:: GROVE_LIGHT_SENSOR

.. option:: CONFIG_GROVE_LIGHT_SENSOR:
.. _CONFIG_GROVE_LIGHT_SENSOR:

Setting this value will enable dirver support for the Grove Light
Sensor.



:Symbol:           GROVE_LIGHT_SENSOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable the Seeed Grove Light Sensor" if SENSOR && GROVE && ADC && NEWLIB_LIBC (value: "n")
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
 * ../drivers/grove/Kconfig:60