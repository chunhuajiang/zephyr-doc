:orphan:

.. title:: IRQ_VECTOR_TABLE_BSP

.. option:: CONFIG_IRQ_VECTOR_TABLE_BSP:
.. _CONFIG_IRQ_VECTOR_TABLE_BSP:

Not user-selectable, helps build system logic.



:Symbol:           IRQ_VECTOR_TABLE_BSP
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

 *  y (value: "y")
 *   Condition: SW_ISR_TABLE || !IRQ_VECTOR_TABLE_CUSTOM (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:254