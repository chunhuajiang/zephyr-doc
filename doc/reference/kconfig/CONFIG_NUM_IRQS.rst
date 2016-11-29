:orphan:

.. title:: NUM_IRQS

.. option:: CONFIG_NUM_IRQS:
.. _CONFIG_NUM_IRQS:

Interrupts available will be 0 to NUM_IRQS-1.
The minimum value is 17 as the first 16 entries in the vector
table are for CPU exceptions.

The BSP must provide a valid default. This drives the size of the
vector table.



:Symbol:           NUM_IRQS
:Type:             int
:Value:            "17"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [17, 256]
:Prompts:

 *  "Upper limit of interrupt numbers/IDs used"
:Default values:

 *  68 (value: "n")
 *   Condition: (none)
 *  36 (value: "n")
 *   Condition: (none)
 *  36 (value: "n")
 *   Condition: (none)
 *  36 (value: "n")
 *   Condition: (none)
 *  86 (value: "n")
 *   Condition: (none)
 *  26 (value: "n")
 *   Condition: (none)
 *  39 (value: "n")
 *   Condition: (none)
 *  179 (value: "n")
 *   Condition: (none)
 *  85 (value: "n")
 *   Condition: (none)
 *  68 (value: "n")
 *   Condition: (none)
 *  59 (value: "n")
 *   Condition: (none)
 *  45 (value: "n")
 *   Condition: (none)
 *  34 (value: "n")
 *   Condition: (none)
 *  45 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../arch/arc/Kconfig:87
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:28
 * ../arch/arc/soc/em11d/Kconfig.defconfig:30
 * ../arch/arc/soc/em7d/Kconfig.defconfig:30
 * ../arch/arc/soc/em9d/Kconfig.defconfig:30
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.series:34
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:35
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.nrf52832:35
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.cc3200:26
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.stm32f401xe:30
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xe:30
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.stm32f103xb:29
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:30
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:34
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:33