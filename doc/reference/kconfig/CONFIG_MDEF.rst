:orphan:

.. title:: MDEF

.. option:: CONFIG_MDEF:
.. _CONFIG_MDEF:

Using an MDEF file can help the startup time of the application since
the objects it lists are statically allocated and initialized, and may
also reduce code size if no subsystem uses the initialization routines.

Disabling this option can reduce the compilation time slightly.

In doubt, select 'y'.



:Symbol:           MDEF
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use MDEF files for statically configured kernel objects"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:308