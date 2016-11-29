:orphan:

.. title:: X86_TSC_RANDOM_GENERATOR

.. option:: CONFIG_X86_TSC_RANDOM_GENERATOR:
.. _CONFIG_X86_TSC_RANDOM_GENERATOR:

This options enables number generator based on timestamp counter
of x86 boards, obtained with rdtsc instruction.



:Symbol:           X86_TSC_RANDOM_GENERATOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "x86 timestamp counter based number generator" if TEST_RANDOM_GENERATOR && X86 (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: TEST_RANDOM_GENERATOR && X86 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/random/Kconfig:40