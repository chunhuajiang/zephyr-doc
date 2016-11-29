:orphan:

.. title:: ISL29035

.. option:: CONFIG_ISL29035:
.. _CONFIG_ISL29035:

Enable driver for the ISL29035 light sensor.



:Symbol:           ISL29035
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ISL29035 light sensor" if SENSOR && I2C && NANO_TIMERS && NANO_TIMEOUTS (value: "n")
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
 * ../drivers/sensor/isl29035/Kconfig:19