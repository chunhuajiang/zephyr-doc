:orphan:

.. title:: I2C_0_NAME

.. option:: CONFIG_I2C_0_NAME:
.. _CONFIG_I2C_0_NAME:

The configuration item CONFIG_I2C_0_NAME:

:Symbol:           I2C_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Select a name for finding the device" if I2C_0 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: I2C_0 (value: "n")
 *  "I2C_0"
 *   Condition: (none)
 *  "I2C_0"
 *   Condition: (none)
 *  "I2C_0"
 *   Condition: (none)
 *  "I2C_0"
 *   Condition: (none)
 *  "I2C_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_X1000 && I2C_DW && I2C_0 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:146
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:150
 * ../arch/arc/soc/em11d/Kconfig.defconfig:149
 * ../arch/arc/soc/em7d/Kconfig.defconfig:149
 * ../arch/arc/soc/em9d/Kconfig.defconfig:147
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:89