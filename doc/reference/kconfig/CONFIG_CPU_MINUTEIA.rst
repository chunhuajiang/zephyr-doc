:orphan:

.. title:: CPU_MINUTEIA

.. option:: CONFIG_CPU_MINUTEIA:
.. _CONFIG_CPU_MINUTEIA:

This option signifies the use of a CPU from the Minute IA family.


:Symbol:           CPU_MINUTEIA
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_IA32 || SOC_SERIES_QUARK_D2000 || SOC_SERIES_QUARK_SE || SOC_SERIES_QUARK_X1000 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 (value: "y")
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:52