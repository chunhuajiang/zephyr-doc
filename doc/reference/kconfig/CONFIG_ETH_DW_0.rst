:orphan:

.. title:: ETH_DW_0

.. option:: CONFIG_ETH_DW_0:
.. _CONFIG_ETH_DW_0:

Include port 0 driver



:Symbol:           ETH_DW_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Synopsys DesignWare Ethernet port 0"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETHERNET && SOC_SERIES_QUARK_X1000 && ETH_DW (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig:47
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:253