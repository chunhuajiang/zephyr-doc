:orphan:

.. title:: IRQ_OFFLOAD

.. option:: CONFIG_IRQ_OFFLOAD:
.. _CONFIG_IRQ_OFFLOAD:

Enable irq_offload() API which allows functions to be synchronously
run in interrupt context. Mainly useful for test cases.



:Symbol:           IRQ_OFFLOAD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable IRQ offload"
 *  "Enable IRQ offload"
 *  "Enable IRQ offload"
 *  "Enable IRQ offload"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
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
 NIOS2 (value: "n")
:Locations:
 * ../arch/arc/Kconfig:146
 * ../arch/x86/Kconfig:249
 * ../arch/arm/core/cortex_m/Kconfig:197
 * ../arch/nios2/Kconfig:50