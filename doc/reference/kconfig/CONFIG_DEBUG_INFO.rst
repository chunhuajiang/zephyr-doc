:orphan:

.. title:: DEBUG_INFO

.. option:: CONFIG_DEBUG_INFO:
.. _CONFIG_DEBUG_INFO:

This option enables the addition of various information that can be used
by debuggers in debugging the system.

NOTE: Does not currently work with the x86 IAMCU ABI.



:Symbol:           DEBUG_INFO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable system debugging information" if X86 && !X86_IAMCU (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: X86 && !X86_IAMCU (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:70