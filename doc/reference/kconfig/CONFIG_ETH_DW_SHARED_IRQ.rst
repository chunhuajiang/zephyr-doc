:orphan:

.. title:: ETH_DW_SHARED_IRQ

.. option:: CONFIG_ETH_DW_SHARED_IRQ:
.. _CONFIG_ETH_DW_SHARED_IRQ:

The configuration item CONFIG_ETH_DW_SHARED_IRQ:

:Symbol:           ETH_DW_SHARED_IRQ
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SHARED_IRQ && ETH_DW && ETH_DW_0_IRQ_SHARED (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ETH_DW (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig:43