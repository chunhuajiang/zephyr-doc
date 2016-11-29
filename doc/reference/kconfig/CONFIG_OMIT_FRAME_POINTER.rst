:orphan:

.. title:: OMIT_FRAME_POINTER

.. option:: CONFIG_OMIT_FRAME_POINTER:
.. _CONFIG_OMIT_FRAME_POINTER:

Prevent the compiler from putting the stack frame pointer into a
register. Saves a few instructions in function prologues/epilogues and
frees up a register for general-purpose use, which can provide good
performance improvements on register-constrained architectures like
x86. Omitting frame pointers impedes debugging as local variables are
harder to locate and it is much more difficult to produce a stack
trace. Recommended only for production builds which do not need to be
debugged.



:Symbol:           OMIT_FRAME_POINTER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Omit frame pointer"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:246