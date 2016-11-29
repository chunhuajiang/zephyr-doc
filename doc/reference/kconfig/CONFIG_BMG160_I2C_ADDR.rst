:orphan:

.. title:: BMG160_I2C_ADDR

.. option:: CONFIG_BMG160_I2C_ADDR:
.. _CONFIG_BMG160_I2C_ADDR:

BMG160 chip's I2C address. Chip supports two addresses: 0x68 and 0x69 (if
SDO pin is pulled to GND).



:Symbol:           BMG160_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMG160 I2C address" if BMG160 (value: "n")
:Default values:

 *  0x68 (value: "n")
 *   Condition: BMG160 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:23