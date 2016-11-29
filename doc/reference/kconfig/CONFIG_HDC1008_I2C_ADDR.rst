:orphan:

.. title:: HDC1008_I2C_ADDR

.. option:: CONFIG_HDC1008_I2C_ADDR:
.. _CONFIG_HDC1008_I2C_ADDR:

0x40: A0 connected GND and A1 connected to GND.
0x41: A0 connected VDD and A1 connected to GND.
0x42: A0 connected GND and A1 connected to VDD.
0x43: A0 connected VDD and A1 connected to VDD.



:Symbol:           HDC1008_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Address for HDC1008" if HDC1008 (value: "n")
:Default values:

 *  "0x40" (value: "n")
 *   Condition: HDC1008 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hdc1008/Kconfig:35