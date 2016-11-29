:orphan:

.. title:: FP_HARDABI

.. option:: CONFIG_FP_HARDABI:
.. _CONFIG_FP_HARDABI:

This option selects the Floating point ABI in which hardware floating
point instructions are generated and uses FPU-specific calling
conventions



:Symbol:           FP_HARDABI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Floating point Hard ABI" if FLOAT (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_HAS_FPU && ARM (value: "n")
:Locations:
 * ../arch/arm/core/Kconfig:71