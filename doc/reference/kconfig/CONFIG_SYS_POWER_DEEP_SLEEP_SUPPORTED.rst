:orphan:

.. title:: SYS_POWER_DEEP_SLEEP_SUPPORTED

.. option:: CONFIG_SYS_POWER_DEEP_SLEEP_SUPPORTED:
.. _CONFIG_SYS_POWER_DEEP_SLEEP_SUPPORTED:

This option signifies that the target supports the SYS_POWER_DEEP_SLEEP
configuration option.



:Symbol:           SYS_POWER_DEEP_SLEEP_SUPPORTED
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
 SOC_SERIES_QUARK_SE || SOC_SERIES_QUARK_X1000 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/Kconfig:54