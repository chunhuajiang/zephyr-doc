:orphan:

.. title:: SOC_SERIES

.. option:: CONFIG_SOC_SERIES:
.. _CONFIG_SOC_SERIES:

SoC series name which can be found under arch/<arch>/soc/<family>/<series>.
This option holds the directory name used by the build system to locate
the correct linker and header files.



:Symbol:           SOC_SERIES
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  quark_d2000 (value: "quark_d2000")
 *   Condition: (none)
 *  quark_se (value: "quark_se")
 *   Condition: (none)
 *  quark_x1000 (value: "quark_x1000")
 *   Condition: (none)
 *  k6x (value: "k6x")
 *   Condition: (none)
 *  nrf51 (value: "nrf51")
 *   Condition: (none)
 *  nrf52 (value: "nrf52")
 *   Condition: (none)
 *  cc32xx (value: "cc32xx")
 *   Condition: (none)
 *  stm32f4 (value: "stm32f4")
 *   Condition: (none)
 *  stm32f1 (value: "stm32f1")
 *   Condition: (none)
 *  beetle (value: "beetle")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_BEETLE (value: "n")
:Locations:
 * ../arch/Kconfig:87
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:19
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:19
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:22
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.series:21
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:22
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.series:22
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.series:8
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:22
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.series:22
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:23