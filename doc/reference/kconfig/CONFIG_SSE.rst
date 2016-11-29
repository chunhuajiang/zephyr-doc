:orphan:

.. title:: SSE

.. option:: CONFIG_SSE:
.. _CONFIG_SSE:

This option enables the use of SSE registers by threads.



:Symbol:           SSE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SSE registers" if FLOAT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: FLOAT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_HAS_FPU && X86 (value: "n")
:Locations:
 * ../arch/x86/Kconfig:114