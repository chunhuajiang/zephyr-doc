:orphan:

.. title:: TH02

.. option:: CONFIG_TH02:
.. _CONFIG_TH02:

Enable driver for the TH02 temperature sensor.



:Symbol:           TH02
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TH02 Temperature Sensor" if SENSOR && I2C && NANO_TIMERS && NANO_TIMEOUTS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C && NANO_TIMERS && NANO_TIMEOUTS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/th02/Kconfig:17