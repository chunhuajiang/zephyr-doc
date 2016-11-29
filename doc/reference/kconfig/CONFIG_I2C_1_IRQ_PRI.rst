:orphan:

.. title:: I2C_1_IRQ_PRI

.. option:: CONFIG_I2C_1_IRQ_PRI:
.. _CONFIG_I2C_1_IRQ_PRI:

IRQ priority.



:Symbol:           I2C_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if I2C_1 && I2C_0_IRQ_DIRECT (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && BOARD_FRDM_K64F && I2C_1 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:189
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:167
 * ../arch/arc/soc/em11d/Kconfig.defconfig:167
 * ../arch/arc/soc/em7d/Kconfig.defconfig:167
 * ../arch/arc/soc/em9d/Kconfig.defconfig:165
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:97
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:110
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:138
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:138