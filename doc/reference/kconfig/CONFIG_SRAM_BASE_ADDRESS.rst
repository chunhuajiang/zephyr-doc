:orphan:

.. title:: SRAM_BASE_ADDRESS

.. option:: CONFIG_SRAM_BASE_ADDRESS:
.. _CONFIG_SRAM_BASE_ADDRESS:

This option specifies the base address of the SRAM on the board.  It is
normally set by the board's defconfig file and the user should generally
avoid modifying it via the menu configuration.



:Symbol:           SRAM_BASE_ADDRESS
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SRAM Base Address"
 *  "SRAM Base Address"
:Default values:

 *  0x4000 (value: "n")
 *   Condition: NSIM (value: "n")
 *  0xa8000400 (value: "n")
 *   Condition: (none)
 *  0x10000000 (value: "n")
 *   Condition: (none)
 *  0x10000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20004000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: (none)
 *  0x20000000 (value: "n")
 *   Condition: !SOC_ATMEL_SAM3X8E (value: "y")
 *  0x20070000 (value: "n")
 *   Condition: SOC_ATMEL_SAM3X8E (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../arch/arc/Kconfig:201
 * ../arch/arm/core/cortex_m/Kconfig:172
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:47
 * ../arch/arc/soc/em11d/Kconfig.defconfig:50
 * ../arch/arc/soc/em7d/Kconfig.defconfig:50
 * ../arch/arc/soc/em9d/Kconfig.defconfig:50
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.series:24
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:29
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.series:25
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.series:11
 * ../arch/arm/soc/st_stm32/Kconfig.defconfig:5
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:38
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:24
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:53