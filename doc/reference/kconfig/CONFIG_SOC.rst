:orphan:

.. title:: SOC

.. option:: CONFIG_SOC:
.. _CONFIG_SOC:

SoC name which can be found under arch/<arch>/soc/<soc name>.
This option holds the directory name used by the build system to locate
the correct linker and header files for the SoC. This option will go away
once all SoCs are using family/series structure.



:Symbol:           SOC
:Type:             string
:Value:            "ia32"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  quark_se_c1000_ss (value: "quark_se_c1000_ss")
 *   Condition: (none)
 *  em11d (value: "em11d")
 *   Condition: (none)
 *  em7d (value: "em7d")
 *   Condition: (none)
 *  em9d (value: "em9d")
 *   Condition: (none)
 *  ia32 (value: "ia32")
 *   Condition: (none)
 *  quark_d2000 (value: "quark_d2000")
 *   Condition: (none)
 *  quark_se_c1000 (value: "quark_se_c1000")
 *   Condition: (none)
 *  curie (value: "curie")
 *   Condition: (none)
 *  quark_x1000 (value: "quark_x1000")
 *   Condition: (none)
 *  atom (value: "atom")
 *   Condition: (none)
 *  mk64f12 (value: "mk64f12")
 *   Condition: (none)
 *  nRF51822_QFAA (value: "nRF51822_QFAA")
 *   Condition: (none)
 *  nRF51822_QFAB (value: "nRF51822_QFAB")
 *   Condition: (none)
 *  nRF51822_QFAC (value: "nRF51822_QFAC")
 *   Condition: (none)
 *  nRF52832 (value: "nRF52832")
 *   Condition: (none)
 *  cc3200 (value: "cc3200")
 *   Condition: (none)
 *  stm32f401xe (value: "stm32f401xe")
 *   Condition: (none)
 *  stm32f103xe (value: "stm32f103xe")
 *   Condition: (none)
 *  stm32f103xb (value: "stm32f103xb")
 *   Condition: (none)
 *  beetle_r0 (value: "beetle_r0")
 *   Condition: (none)
 *  ti_lm3s6965 (value: "ti_lm3s6965")
 *   Condition: (none)
 *  atmel_sam3 (value: "atmel_sam3")
 *   Condition: (none)
 *  nios2-qemu (value: "nios2-qemu")
 *   Condition: (none)
 *  nios2f-zephyr (value: "nios2f-zephyr")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_NIOS2F_ZEPHYR (value: "n")
:Locations:
 * ../arch/Kconfig:79
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:20
 * ../arch/arc/soc/em11d/Kconfig.defconfig:20
 * ../arch/arc/soc/em7d/Kconfig.defconfig:20
 * ../arch/arc/soc/em9d/Kconfig.defconfig:20
 * ../arch/x86/soc/ia32/Kconfig.defconfig:21
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.quark_d2000:21
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.quark_se_c1000:21
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.curie:21
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.quark_x1000:21
 * ../arch/x86/soc/atom/Kconfig.defconfig:21
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:21
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAA:21
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAB:21
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.nrf51822_QFAC:21
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.nrf52832:21
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:6
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.stm32f401xe:20
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xe:20
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xb:20
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.beetle_r0:21
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:21
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:22
 * ../arch/nios2/soc/nios2-qemu/Kconfig.defconfig:3
 * ../arch/nios2/soc/nios2f-zephyr/Kconfig.defconfig:3