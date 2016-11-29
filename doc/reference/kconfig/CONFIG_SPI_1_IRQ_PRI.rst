:orphan:

.. title:: SPI_1_IRQ_PRI

.. option:: CONFIG_SPI_1_IRQ_PRI:
.. _CONFIG_SPI_1_IRQ_PRI:

The configuration item CONFIG_SPI_1_IRQ_PRI:

:Symbol:           SPI_1_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 interrupt priority" if SPI_1 (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:134
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:229
 * ../arch/arc/soc/em11d/Kconfig.defconfig:250
 * ../arch/arc/soc/em7d/Kconfig.defconfig:250
 * ../arch/arc/soc/em9d/Kconfig.defconfig:248
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:167
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:190
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:163
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:163