:orphan:

.. title:: I2C_0_IRQ_PRI

.. option:: CONFIG_I2C_0_IRQ_PRI:
.. _CONFIG_I2C_0_IRQ_PRI:

IRQ priority.



:Symbol:           I2C_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if I2C_0 && I2C_0_IRQ_DIRECT (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
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
 I2C && BOARD_FRDM_K64F && I2C_0 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:162
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:156
 * ../arch/arc/soc/em11d/Kconfig.defconfig:153
 * ../arch/arc/soc/em7d/Kconfig.defconfig:153
 * ../arch/arc/soc/em9d/Kconfig.defconfig:151
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:116
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:86
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:93
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:104
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:125
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:125