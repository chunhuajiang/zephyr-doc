:orphan:

.. title:: I2C_0_DEFAULT_CFG

.. option:: CONFIG_I2C_0_DEFAULT_CFG:
.. _CONFIG_I2C_0_DEFAULT_CFG:

Allows the I2C port to be brought up with a default configuration.
This is useful to set if other drivers depend upon using the I2C bus
before the application has a chance to custom configure the port.
Setting this value does not prohibit the application from customizing
the values later.  Refer to the I2C datasheet for proper values.



:Symbol:           I2C_0_DEFAULT_CFG
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C default configuration" if I2C_0 (value: "n")
:Default values:

 *  0x0 (value: "n")
 *   Condition: I2C_0 (value: "n")
 *  0x12 (value: "n")
 *   Condition: (none)
 *  0x3 (value: "n")
 *   Condition: (none)
 *  0x3 (value: "n")
 *   Condition: (none)
 *  0x3 (value: "n")
 *   Condition: (none)
 *  0x12 (value: "n")
 *   Condition: (none)
 *  0x12 (value: "n")
 *   Condition: (none)
 *  0x12 (value: "n")
 *   Condition: (none)
 *  0x12 (value: "n")
 *   Condition: (none)
 *  0x12 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && BOARD_FRDM_K64F && I2C_0 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:151
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:153
 * ../arch/arc/soc/em11d/Kconfig.defconfig:151
 * ../arch/arc/soc/em7d/Kconfig.defconfig:151
 * ../arch/arc/soc/em9d/Kconfig.defconfig:149
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:118
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:88
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:91
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:122
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:122