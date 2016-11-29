:orphan:

.. title:: I2C_SS_SDA_HOLD

.. option:: CONFIG_I2C_SS_SDA_HOLD:
.. _CONFIG_I2C_SS_SDA_HOLD:

The hold time on the data signal after a negative edge of i2c clock.
The unit is i2c module base clock.



:Symbol:           I2C_SS_SDA_HOLD
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

 *  10 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_QUARK_SE_C1000_SS (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:195
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:175