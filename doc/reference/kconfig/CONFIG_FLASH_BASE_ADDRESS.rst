:orphan:

.. title:: FLASH_BASE_ADDRESS

.. option:: CONFIG_FLASH_BASE_ADDRESS:
.. _CONFIG_FLASH_BASE_ADDRESS:

This option specifies the base address of the flash on the board.  It is
normally set by the board's defconfig file and the user should generally
avoid modifying it via the menu configuration.


:Symbol:           FLASH_BASE_ADDRESS
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Flash Base Address"
 *  "Flash Base Address"
:Default values:

 *  0x40000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x08000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00080000 (value: "n")
 *   Condition: (none)
 *  0x40034000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ARDUINO_101_SSS (value: "n")
:Locations:
 * ../arch/arc/Kconfig:215
 * ../arch/arm/core/cortex_m/Kconfig:186
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:41
 * ../arch/arc/soc/em11d/Kconfig.defconfig:43
 * ../arch/arc/soc/em7d/Kconfig.defconfig:43
 * ../arch/arc/soc/em9d/Kconfig.defconfig:43
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.series:27
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:32
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.series:28
 * ../arch/arm/soc/st_stm32/Kconfig.defconfig:8
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:41
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:27
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:65
 * ../boards/arc/arduino_101_sss/Kconfig.defconfig:12