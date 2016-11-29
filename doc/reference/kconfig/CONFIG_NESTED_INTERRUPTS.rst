:orphan:

.. title:: NESTED_INTERRUPTS

.. option:: CONFIG_NESTED_INTERRUPTS:
.. _CONFIG_NESTED_INTERRUPTS:

This option enables support for nested interrupts.



:Symbol:           NESTED_INTERRUPTS
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable nested interrupts"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:21