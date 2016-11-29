:orphan:

.. title:: SRAM_SIZE

.. option:: CONFIG_SRAM_SIZE:
.. _CONFIG_SRAM_SIZE:

This option specifies the size of the SRAM in kB.  It is normally set by
the board's defconfig file and the user should generally avoid modifying
it via the menu configuration.



:Symbol:           SRAM_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SRAM Size in kB"
 *  "SRAM Size in kB"
:Default values:

 *  16 (value: "n")
 *   Condition: NSIM (value: "n")
 *  24 (value: "n")
 *   Condition: (none)
 *  131072 (value: "n")
 *   Condition: (none)
 *  131072 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  16 (value: "n")
 *   Condition: (none)
 *  16 (value: "n")
 *   Condition: (none)
 *  32 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: (none)
 *  240 (value: "n")
 *   Condition: (none)
 *  96 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: (none)
 *  20 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: (none)
 *  96 (value: "n")
 *   Condition: SOC_ATMEL_SAM3X8E (value: "n")
 *  192 (value: "n")
 *   Condition: (none)
 *  192 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arc/Kconfig:194
 * ../arch/arm/core/cortex_m/Kconfig:165
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:51
 * ../arch/arc/soc/em11d/Kconfig.defconfig:53
 * ../arch/arc/soc/em7d/Kconfig.defconfig:53
 * ../arch/arc/soc/em9d/Kconfig.defconfig:53
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAA:25
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAB:25
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAC:25
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.nrf52832:29
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:14
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.stm32f401xe:24
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xe:24
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xb:23
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.beetle_r0:28
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:50
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:26
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:26