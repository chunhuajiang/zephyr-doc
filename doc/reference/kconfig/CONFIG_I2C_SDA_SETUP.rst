:orphan:

.. title:: I2C_SDA_SETUP

.. option:: CONFIG_I2C_SDA_SETUP:
.. _CONFIG_I2C_SDA_SETUP:

The delay time of clock rising edge relative to i2c data signal change.
The unit is i2c module base clock.



:Symbol:           I2C_SDA_SETUP
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

 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:202
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:172
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:122
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:104