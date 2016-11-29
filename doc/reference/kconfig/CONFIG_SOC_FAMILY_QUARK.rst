:orphan:

.. title:: SOC_FAMILY_QUARK

.. option:: CONFIG_SOC_FAMILY_QUARK:
.. _CONFIG_SOC_FAMILY_QUARK:

The configuration item CONFIG_SOC_FAMILY_QUARK:

:Symbol:           SOC_FAMILY_QUARK
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
 SOC_SERIES_QUARK_D2000 || SOC_SERIES_QUARK_SE || SOC_SERIES_QUARK_X1000 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/soc/intel_quark/Kconfig:17