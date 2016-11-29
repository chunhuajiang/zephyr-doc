:orphan:

.. title:: NUM_IRQ_PRIO_LEVELS

.. option:: CONFIG_NUM_IRQ_PRIO_LEVELS:
.. _CONFIG_NUM_IRQ_PRIO_LEVELS:

Interrupt priorities available will be 0 to NUM_IRQ_PRIO_LEVELS-1.
The minimum value is 1.

The BSP must provide a valid default for proper operation.



:Symbol:           NUM_IRQ_PRIO_LEVELS
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 16]
:Prompts:

 *  "Number of supported interrupt priority levels"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:77
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:23
 * ../arch/arc/soc/em11d/Kconfig.defconfig:23
 * ../arch/arc/soc/em7d/Kconfig.defconfig:23
 * ../arch/arc/soc/em9d/Kconfig.defconfig:23