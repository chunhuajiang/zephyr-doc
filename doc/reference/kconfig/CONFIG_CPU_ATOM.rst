:orphan:

.. title:: CPU_ATOM

.. option:: CONFIG_CPU_ATOM:
.. _CONFIG_CPU_ATOM:

This option signifies the use of a CPU from the Atom family.



:Symbol:           CPU_ATOM
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
 (no default values)
:Selects:

 *  :option:`CONFIG_CMOV`
 *  :option:`CONFIG_CPU_HAS_FPU`
:Reverse (select-related) dependencies:
 SOC_ATOM (value: "n")
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:44