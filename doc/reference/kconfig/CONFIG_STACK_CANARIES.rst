:orphan:

.. title:: STACK_CANARIES

.. option:: CONFIG_STACK_CANARIES:
.. _CONFIG_STACK_CANARIES:

This option enables compiler stack canaries support kernel functions.

If stack canaries are supported by the compiler, it will emit
extra code that inserts a canary value into the stack frame when
a function is entered and validates this value upon exit.
Stack corruption (such as that caused by buffer overflow) results
in a fatal error condition for the running entity.
Enabling this option can result in a significant increase
in footprint and an associated decrease in performance.

If stack canaries are not supported by the compiler, enabling this
option has no effect.


:Symbol:           STACK_CANARIES
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Compiler stack canaries"
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
 * ../kernel/Kconfig:203