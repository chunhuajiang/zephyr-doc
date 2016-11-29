:orphan:

.. title:: TMP112_I2C_ADDR

.. option:: CONFIG_TMP112_I2C_ADDR:
.. _CONFIG_TMP112_I2C_ADDR:

I2C address of the TMP112 sensor.

0x48: A0 connected GND and A1 connected to GND.
0x49: A0 connected VDD and A1 connected to GND.
0x4A: A0 connected SDA and A1 connected to GND.
0x4B: A0 connected SCL and A1 connected to GND.




:Symbol:           TMP112_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C address for TMP112" if TMP112 (value: "n")
:Default values:

 *  0x48 (value: "n")
 *   Condition: TMP112 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp112/Kconfig:35