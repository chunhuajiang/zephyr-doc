:orphan:

.. title:: SPI_DW_ARC_AUX_REGS

.. option:: CONFIG_SPI_DW_ARC_AUX_REGS:
.. _CONFIG_SPI_DW_ARC_AUX_REGS:

SPI IP block registers are part of user extended auxiliary
registers and thus their access is different than memory
mapped registers.




:Symbol:           SPI_DW_ARC_AUX_REGS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Registers are part of ARC auxiliary registers" if SPI_DW && ARC (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: SPI_DW && ARC (value: "n")
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_EM9D && SPI_DW (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:29
 * ../arch/arc/soc/em11d/Kconfig.defconfig:232
 * ../arch/arc/soc/em7d/Kconfig.defconfig:232
 * ../arch/arc/soc/em9d/Kconfig.defconfig:230