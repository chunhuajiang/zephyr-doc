:orphan:

.. title:: LPS25HB

.. option:: CONFIG_LPS25HB:
.. _CONFIG_LPS25HB:

Enable driver for LPS25HB I2C-based pressure and temperature
sensor.



:Symbol:           LPS25HB
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LPS25HB pressure and temperature" if SENSOR && I2C (value: "n")
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
 * ../drivers/sensor/lps25hb/Kconfig:17