:orphan:

.. title:: FP_SOFTABI

.. option:: CONFIG_FP_SOFTABI:
.. _CONFIG_FP_SOFTABI:

This option selects the Floating point ABI in which hardware floating
point instructions are generated but soft-float calling conventions.



:Symbol:           FP_SOFTABI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Floating point Soft ABI" if FLOAT (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_HAS_FPU && ARM (value: "n")
:Locations:
 * ../arch/arm/core/Kconfig:79