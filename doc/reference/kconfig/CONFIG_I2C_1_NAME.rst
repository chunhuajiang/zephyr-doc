:orphan:

.. title:: I2C_1_NAME

.. option:: CONFIG_I2C_1_NAME:
.. _CONFIG_I2C_1_NAME:

The configuration item CONFIG_I2C_1_NAME:

:Symbol:           I2C_1_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Select a name for finding the device" if I2C_1 (value: "n")
:Default values:

 *  "I2C_1"
 *   Condition: I2C_1 (value: "n")
 *  "I2C_1"
 *   Condition: (none)
 *  "I2C_1"
 *   Condition: (none)
 *  "I2C_1"
 *   Condition: (none)
 *  "I2C_1"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_EM9D && I2C_DW && I2C_1 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:173
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:161
 * ../arch/arc/soc/em11d/Kconfig.defconfig:163
 * ../arch/arc/soc/em7d/Kconfig.defconfig:163
 * ../arch/arc/soc/em9d/Kconfig.defconfig:161