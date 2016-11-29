:orphan:

.. title:: ARC_INIT

.. option:: CONFIG_ARC_INIT:
.. _CONFIG_ARC_INIT:

Allows x86 processor to kickoff the ARC slave processor.



:Symbol:           ARC_INIT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE ARC Kickoff"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:35