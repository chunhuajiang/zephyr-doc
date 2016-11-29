:orphan:

.. title:: FLOAT

.. option:: CONFIG_FLOAT:
.. _CONFIG_FLOAT:

This option allows tasks and fibers to use the floating point registers.
By default, only a single task or fiber may use the registers.

Disabling this option means that any task or fiber that uses a
floating point register will get a fatal exception.



:Symbol:           FLOAT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Floating point registers"
 *  "Floating point registers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_HAS_FPU && ARM (value: "n")
:Locations:
 * ../arch/x86/Kconfig:86
 * ../arch/arm/core/Kconfig:46