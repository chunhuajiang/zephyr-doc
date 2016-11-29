:orphan:

.. title:: ETH_DW

.. option:: CONFIG_ETH_DW:
.. _CONFIG_ETH_DW:

Enable Synopsys DesignWare Ethernet driver.



:Symbol:           ETH_DW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Synopsys DesignWare Ethernet driver" if ETHERNET (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ETHERNET (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETHERNET && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig:34
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:248