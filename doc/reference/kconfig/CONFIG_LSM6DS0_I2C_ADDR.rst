:orphan:

.. title:: LSM6DS0_I2C_ADDR

.. option:: CONFIG_LSM6DS0_I2C_ADDR:
.. _CONFIG_LSM6DS0_I2C_ADDR:

I2C address of the LSM6DS0 sensor.
Use 0x6A if the SA0 pin is pulled to GND or 0x6B if the SA0 pin
is pulled to VCC.



:Symbol:           LSM6DS0_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "LSM6DS0 I2C address" if LSM6DS0 (value: "n")
:Default values:

 *  0x6B (value: "n")
 *   Condition: LSM6DS0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:52