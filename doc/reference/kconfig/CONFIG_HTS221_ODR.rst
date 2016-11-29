:orphan:

.. title:: HTS221_ODR

.. option:: CONFIG_HTS221_ODR:
.. _CONFIG_HTS221_ODR:

Sensor output data rate expressed in samples per second.
Data rates supported by the chip are 1, 7 and 12.5.


:Symbol:           HTS221_ODR
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Output data rate" if HTS221 (value: "n")
:Default values:

 *  "1"
 *   Condition: HTS221 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:105