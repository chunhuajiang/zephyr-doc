:orphan:

.. title:: SX9500_I2C_ADDR

.. option:: CONFIG_SX9500_I2C_ADDR:
.. _CONFIG_SX9500_I2C_ADDR:

Specify the I2C slave address for the SX9500.



:Symbol:           SX9500_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SX9500 I2C slave address" if SX9500 (value: "n")
:Default values:

 *  0x2B (value: "n")
 *   Condition: SX9500 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:31