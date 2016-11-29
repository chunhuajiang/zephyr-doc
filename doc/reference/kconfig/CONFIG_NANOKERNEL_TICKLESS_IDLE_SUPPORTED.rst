:orphan:

.. title:: NANOKERNEL_TICKLESS_IDLE_SUPPORTED

.. option:: CONFIG_NANOKERNEL_TICKLESS_IDLE_SUPPORTED:
.. _CONFIG_NANOKERNEL_TICKLESS_IDLE_SUPPORTED:

To be selected by an architecture if it does support tickless idle in
nanokernel systems.



:Symbol:           NANOKERNEL_TICKLESS_IDLE_SUPPORTED
:Type:             bool
:Value:            "y"
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
 X86 || CPU_ARCV2 && ARC (value: "y")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:185