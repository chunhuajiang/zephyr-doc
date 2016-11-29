:orphan:

.. title:: IA32_LEGACY_IO_PORTS

.. option:: CONFIG_IA32_LEGACY_IO_PORTS:
.. _CONFIG_IA32_LEGACY_IO_PORTS:

This option enables IA32 legacy IO ports. Note these are much slower
than memory access, so they should be used in last resort.



:Symbol:           IA32_LEGACY_IO_PORTS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Support IA32 legacy IO ports" if ISA_IA32 (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: ISA_IA32 (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:160