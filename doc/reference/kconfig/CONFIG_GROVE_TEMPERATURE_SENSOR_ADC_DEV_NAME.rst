:orphan:

.. title:: GROVE_TEMPERATURE_SENSOR_ADC_DEV_NAME

.. option:: CONFIG_GROVE_TEMPERATURE_SENSOR_ADC_DEV_NAME:
.. _CONFIG_GROVE_TEMPERATURE_SENSOR_ADC_DEV_NAME:

Specify the device name of the ADC to which the Grove Temperature
Sensor is connected.



:Symbol:           GROVE_TEMPERATURE_SENSOR_ADC_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ADC where Grove Temperature Sensor is connected" if GROVE_TEMPERATURE_SENSOR (value: "n")
:Default values:

 *  "ADC_0"
 *   Condition: GROVE_TEMPERATURE_SENSOR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/grove/Kconfig:134