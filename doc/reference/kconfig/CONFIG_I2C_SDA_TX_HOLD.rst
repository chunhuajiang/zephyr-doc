:orphan:

.. title:: I2C_SDA_TX_HOLD

.. option:: CONFIG_I2C_SDA_TX_HOLD:
.. _CONFIG_I2C_SDA_TX_HOLD:

The hold time on the data signal after a negative edge of i2c clock
while i2c acts as transmitter.
The unit is i2c module base clock.



:Symbol:           I2C_SDA_TX_HOLD
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  16 (value: "n")
 *   Condition: (none)
 *  16 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:209
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:125
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:107