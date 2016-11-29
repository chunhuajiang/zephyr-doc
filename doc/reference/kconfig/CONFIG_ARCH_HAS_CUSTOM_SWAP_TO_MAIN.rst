:orphan:

.. title:: ARCH_HAS_CUSTOM_SWAP_TO_MAIN

.. option:: CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN:
.. _CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN:

It's possible that an architecture port cannot use _Swap() to swap to
the _main() thread, but instead must do something custom. It must
enable this option in that case.


:Symbol:           ARCH_HAS_CUSTOM_SWAP_TO_MAIN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 CPU_CORTEX_M && ARM (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:358