:orphan:

.. title:: ETH_DW_0_IRQ_PRI

.. option:: CONFIG_ETH_DW_0_IRQ_PRI:
.. _CONFIG_ETH_DW_0_IRQ_PRI:

IRQ priority



:Symbol:           ETH_DW_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if ETH_DW_0 && ETH_DW_0_IRQ_DIRECT (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: ETH_DW_0 && ETH_DW_0_IRQ_DIRECT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_DW (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig:86