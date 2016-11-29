:orphan:

.. title:: SYS_CLOCK_HW_CYCLES_PER_SEC

.. option:: CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC:
.. _CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC:

This option specifies the frequency of the hardware timer used for the
system clock (in Hz). This option is set by the board's Kconfig file
and the user should generally avoid modifying it via the menu configuration.



:Symbol:           SYS_CLOCK_HW_CYCLES_PER_SEC
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "System clock's h/w timer frequency"
:Default values:

 *  32000000 (value: "n")
 *   Condition: (none)
 *  20000000 (value: "n")
 *   Condition: (none)
 *  30000000 (value: "n")
 *   Condition: (none)
 *  20000000 (value: "n")
 *   Condition: (none)
 *  150000000 (value: "n")
 *   Condition: LOAPIC_TIMER (value: "n")
 *  25000000 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
 *  32000000 (value: "n")
 *   Condition: (none)
 *  32000000 (value: "n")
 *   Condition: (none)
 *  25000000 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
 *  150000000 (value: "n")
 *   Condition: LOAPIC_TIMER (value: "n")
 *  25000000 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
 *  32768 (value: "n")
 *   Condition: (none)
 *  64000000 (value: "n")
 *   Condition: (none)
 *  80000000 (value: "n")
 *   Condition: (none)
 *  24000000 (value: "n")
 *   Condition: (none)
 *  12000000 (value: "n")
 *   Condition: (none)
 *  84000000 (value: "n")
 *   Condition: (none)
 *  50000000 (value: "n")
 *   Condition: (none)
 *  50000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_NIOS2F_ZEPHYR (value: "n")
:Locations:
 * ../kernel/Kconfig:40
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:35
 * ../arch/arc/soc/em11d/Kconfig.defconfig:37
 * ../arch/arc/soc/em7d/Kconfig.defconfig:37
 * ../arch/arc/soc/em9d/Kconfig.defconfig:37
 * ../arch/x86/soc/ia32/Kconfig.defconfig:37
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:29
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:41
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:37
 * ../arch/x86/soc/atom/Kconfig.defconfig:37
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:25
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.nrf52832:25
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:10
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:34
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:40
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:37
 * ../arch/nios2/soc/nios2-qemu/Kconfig.defconfig:7
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:7