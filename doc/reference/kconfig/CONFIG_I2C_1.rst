:orphan:

.. title:: I2C_1

.. option:: CONFIG_I2C_1:
.. _CONFIG_I2C_1:

The configuration item CONFIG_I2C_1:

:Symbol:           I2C_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable I2C Port 1" if I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:168
 * ../arch/arc/soc/em11d/Kconfig.defconfig:158
 * ../arch/arc/soc/em7d/Kconfig.defconfig:158
 * ../arch/arc/soc/em9d/Kconfig.defconfig:156
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:93
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:107
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:130
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:130