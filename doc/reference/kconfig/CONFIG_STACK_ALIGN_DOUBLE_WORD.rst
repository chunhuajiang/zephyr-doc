:orphan:

.. title:: STACK_ALIGN_DOUBLE_WORD

.. option:: CONFIG_STACK_ALIGN_DOUBLE_WORD:
.. _CONFIG_STACK_ALIGN_DOUBLE_WORD:

This is needed to conform to AAPCS, the procedure call standard for
the ARM. It wastes stack space.



:Symbol:           STACK_ALIGN_DOUBLE_WORD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Align stacks on double-words (8 octets)"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:118