:orphan:

.. title:: MAX44009_I2C_ADDR

.. option:: CONFIG_MAX44009_I2C_ADDR:
.. _CONFIG_MAX44009_I2C_ADDR:

I2C address of the MAX44009 sensor. Possible configurations:

0x4a: A0 connected to GND.
0x4b: A0 connected to VCC.



:Symbol:           MAX44009_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "MAX44009 I2C address" if MAX44009 (value: "n")
:Default values:

 *  "0x4a" (value: "n")
 *   Condition: MAX44009 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/max44009/Kconfig:36