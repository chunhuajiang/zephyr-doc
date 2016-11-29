:orphan:

.. title:: SPI_DW_CLOCK_GATE

.. option:: CONFIG_SPI_DW_CLOCK_GATE:
.. _CONFIG_SPI_DW_CLOCK_GATE:

The configuration item CONFIG_SPI_DW_CLOCK_GATE:

:Symbol:           SPI_DW_CLOCK_GATE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable glock gating" if SPI_DW && SOC_QUARK_SE_C1000 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI_DW && SOC_QUARK_SE_C1000 (value: "n")
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CLOCK_CONTROL` if SPI_DW && SOC_QUARK_SE_C1000 (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_EM9D && SPI_DW (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:55
 * ../arch/arc/soc/em11d/Kconfig.defconfig:226
 * ../arch/arc/soc/em7d/Kconfig.defconfig:226
 * ../arch/arc/soc/em9d/Kconfig.defconfig:224