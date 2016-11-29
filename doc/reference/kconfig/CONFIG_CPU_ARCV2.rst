:orphan:

.. title:: CPU_ARCV2

.. option:: CONFIG_CPU_ARCV2:
.. _CONFIG_CPU_ARCV2:

This option signifies the use of a CPU of the ARCv2 family.



:Symbol:           CPU_ARCV2
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

 *  :option:`CONFIG_NANOKERNEL_TICKLESS_IDLE_SUPPORTED`
:Reverse (select-related) dependencies:
 CPU_ARCEM4 && ARC (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:51