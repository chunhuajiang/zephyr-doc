:orphan:

.. title:: TMP007_I2C_ADDR

.. option:: CONFIG_TMP007_I2C_ADDR:
.. _CONFIG_TMP007_I2C_ADDR:

I2C address of the TMP007 sensor.

0x40: A0 connected GND and A1 connected to GND.
0x41: A0 connected VDD and A1 connected to GND.
0x42: A0 connected SDA and A1 connected to GND.
0x43: A0 connected SCL and A1 connected to GND.
0x44: A0 connected GND and A1 connected to VDD.
0x45: A0 connected VDD and A1 connected to VDD.
0x46: A0 connected SDA and A1 connected to VDD.
0x47: A0 connected SCL and A1 connected to VDD.



:Symbol:           TMP007_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C address for TMP006 Sensor" if TMP007 (value: "n")
:Default values:

 *  "0x40" (value: "n")
 *   Condition: TMP007 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:35