:orphan:

.. title:: NUM_IRQ_PRIO_BITS

.. option:: CONFIG_NUM_IRQ_PRIO_BITS:
.. _CONFIG_NUM_IRQ_PRIO_BITS:

Cortex-M chips can implement up to 8 bits of interrupt priorities,
for a maximum of 256 priorities. Most chips implement fewer than 8.

The board must define the correct value.



:Symbol:           NUM_IRQ_PRIO_BITS
:Type:             int
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

 *  4 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
 *   Condition: (none)
 *  4 (value: "n")
 *   Condition: (none)
 *  4 (value: "n")
 *   Condition: (none)
 *  3 (value: "n")
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
 SOC_ATMEL_SAM3 (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:126
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.series:30
 * ../arch/arm/soc/nordic_nrf5/nrf51/Kconfig.defconfig.series:39
 * ../arch/arm/soc/nordic_nrf5/nrf52/Kconfig.defconfig.series:31
 * ../arch/arm/soc/ti_simplelink/cc32xx/Kconfig.defconfig.series:14
 * ../arch/arm/soc/st_stm32/stm32f4/Kconfig.defconfig.series:25
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.series:25
 * ../arch/arm/soc/arm/beetle/Kconfig.defconfig.series:26
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:30
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:25