:orphan:

.. title:: SPI_DW_FIFO_DEPTH

.. option:: CONFIG_SPI_DW_FIFO_DEPTH:
.. _CONFIG_SPI_DW_FIFO_DEPTH:

Corresponds to the SSI_TX_FIFO_DEPTH and
SSI_RX_FIFO_DEPTH of the DesignWare Syncrhonous
Serial Interface. Depth ranges from 2-256.



:Symbol:           SPI_DW_FIFO_DEPTH
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Rx and Tx FIFO Depth"
:Default values:

 *  32 (value: "n")
 *   Condition: (none)
 *  32 (value: "n")
 *   Condition: (none)
 *  32 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_EM9D && SPI_DW (value: "n")
:Locations:
 * ../drivers/spi/Kconfig.dw:66
 * ../arch/arc/soc/em11d/Kconfig.defconfig:229
 * ../arch/arc/soc/em7d/Kconfig.defconfig:229
 * ../arch/arc/soc/em9d/Kconfig.defconfig:227