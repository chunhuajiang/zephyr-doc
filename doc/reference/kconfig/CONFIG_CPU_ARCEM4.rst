:orphan:

.. title:: CPU_ARCEM4

.. option:: CONFIG_CPU_ARCEM4:
.. _CONFIG_CPU_ARCEM4:

This option signifies the use of an ARC EM4 CPU



:Symbol:           CPU_ARCEM4
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
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CPU_ARCV2`
 *  :option:`CONFIG_ATOMIC_OPERATIONS_C`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:39