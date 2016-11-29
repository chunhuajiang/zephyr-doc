:orphan:

.. title:: FLASH_SIZE

.. option:: CONFIG_FLASH_SIZE:
.. _CONFIG_FLASH_SIZE:

This option specifies the size of the flash in kB.  It is normally set by
the board's defconfig file and the user should generally avoid modifying
it via the menu configuration.



:Symbol:           FLASH_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Flash Size in kB"
 *  "Flash Size in kB"
:Default values:

 *  152 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  256 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: (none)
 *  256 (value: "n")
 *   Condition: (none)
 *  512 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: (none)
 *  512 (value: "n")
 *   Condition: (none)
 *  512 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: (none)
 *  256 (value: "n")
 *   Condition: (none)
 *  512 (value: "n")
 *   Condition: SOC_ATMEL_SAM3X8E (value: "n")
 *  128 (value: "n")
 *   Condition: (none)
 *  1024 (value: "n")
 *   Condition: (none)
 *  1024 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../arch/arc/Kconfig:208
 * ../arch/arm/core/cortex_m/Kconfig:179
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:44
 * ../arch/arc/soc/em11d/Kconfig.defconfig:46
 * ../arch/arc/soc/em7d/Kconfig.defconfig:46
 * ../arch/arc/soc/em9d/Kconfig.defconfig:46
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAA:28
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAB:28
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAC:28
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.nrf52832:32
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:17
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.stm32f401xe:27
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xe:27
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xb:26
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.beetle_r0:34
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:62
 * ../boards/arc/arduino_101_sss/Kconfig.defconfig:8
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:23
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:23