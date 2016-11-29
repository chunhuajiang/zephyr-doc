:orphan:

.. title:: MPU9150

.. option:: CONFIG_MPU9150:
.. _CONFIG_MPU9150:

Enable this config option if the AK8975 sensor is part of a
MPU9150 chip.



:Symbol:           MPU9150
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable MPU9180 support" if AK8975 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: AK8975 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/ak8975/Kconfig:61