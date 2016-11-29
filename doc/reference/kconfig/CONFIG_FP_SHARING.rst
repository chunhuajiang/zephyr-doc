:orphan:

.. title:: FP_SHARING

.. option:: CONFIG_FP_SHARING:
.. _CONFIG_FP_SHARING:

This option allows multiple tasks and fibers to use the floating point
registers.



:Symbol:           FP_SHARING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Floating point register sharing" if FLOAT (value: "n")
 *  "Floating point register sharing" if FLOAT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: FLOAT (value: "n")
 *  n (value: "n")
 *   Condition: FLOAT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_HAS_FPU && ARM (value: "n")
:Locations:
 * ../arch/x86/Kconfig:101
 * ../arch/arm/core/Kconfig:57