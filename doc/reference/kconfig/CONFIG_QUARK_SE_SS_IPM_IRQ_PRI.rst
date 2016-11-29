:orphan:

.. title:: QUARK_SE_SS_IPM_IRQ_PRI

.. option:: CONFIG_QUARK_SE_SS_IPM_IRQ_PRI:
.. _CONFIG_QUARK_SE_SS_IPM_IRQ_PRI:

Priority level for interrupts coming in from the inter-processor
mailboxes.



:Symbol:           QUARK_SE_SS_IPM_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IPM interrupt priority"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC && SOC_QUARK_SE_C1000_SS && ARC && IPM (value: "n")
:Locations:
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig:20