:orphan:

.. title:: CMOV

.. option:: CONFIG_CMOV:
.. _CONFIG_CMOV:

This option signifies the use of an Intel CPU that supports
the CMOV instruction.



:Symbol:           CMOV
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

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 CPU_ATOM && X86 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:169