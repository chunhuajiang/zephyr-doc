:orphan:

.. title:: SOC_FAMILY

.. option:: CONFIG_SOC_FAMILY:
.. _CONFIG_SOC_FAMILY:

SoC family name which can be found under arch/<arch>/soc/<family>.
This option holds the directory name used by the build system to locate
the correct linker and header files.



:Symbol:           SOC_FAMILY
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

 *  "intel_quark"
 *   Condition: (none)
 *  "nxp_kinetis"
 *   Condition: (none)
 *  nordic_nrf5 (value: "nordic_nrf5")
 *   Condition: (none)
 *  ti_simplelink (value: "ti_simplelink")
 *   Condition: (none)
 *  st_stm32 (value: "st_stm32")
 *   Condition: (none)
 *  arm (value: "arm")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_ARM && ARM (value: "n")
:Locations:
 * ../arch/Kconfig:94
 * ../arch/x86/soc/intel_quark/Kconfig:22
 * ../arch/arm/soc/nxp_kinetis/Kconfig:24
 * ../arch/arm/soc/nordic_nrf5/Kconfig:24
 * ../arch/arm/soc/ti_simplelink/Kconfig:10
 * ../arch/arm/soc/st_stm32/Kconfig:24
 * ../arch/arm/soc/arm/Kconfig:24