:orphan:

.. title:: DEBUG_IRQS

.. option:: CONFIG_DEBUG_IRQS:
.. _CONFIG_DEBUG_IRQS:

Enable additional debugging services for interrupts. May nontrivially
increase ROM size, so use only when you need it.



:Symbol:           DEBUG_IRQS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Extra interrupt debugging functionality"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:115