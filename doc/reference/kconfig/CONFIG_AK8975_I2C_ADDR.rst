:orphan:

.. title:: AK8975_I2C_ADDR

.. option:: CONFIG_AK8975_I2C_ADDR:
.. _CONFIG_AK8975_I2C_ADDR:

I2C address of the AK8975 sensor. Choose:

- 0x0C if CAD1 connected to GND nad CAD0 is connected to GND
- 0x0D if CAD1 connected to GND nad CAD0 is connected to VDD
- 0x0E if CAD1 connected to VDD nad CAD0 is connected to GND
- 0x0F if CAD1 connected to VDD nad CAD0 is connected to VDD

If the AK8975 sensor is part of a MPU9159 chip, the I2C address
needs to be 0x0C.



:Symbol:           AK8975_I2C_ADDR
:Type:             hex
:Value:            "0xc"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0x0C, 0x0F]
:Prompts:

 *  "I2C address" if AK8975 (value: "n")
:Default values:

 *  0x0C (value: "n")
 *   Condition: AK8975 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/ak8975/Kconfig:35