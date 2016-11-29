:orphan:

.. title:: SX9500

.. option:: CONFIG_SX9500:
.. _CONFIG_SX9500:

Enable driver for SX9500 I2C-based SAR proximity sensor.



:Symbol:           SX9500
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SX9500 I2C SAR Proximity Chip" if SENSOR && I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:19