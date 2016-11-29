:orphan:

.. title:: SYS_POWER_LOW_POWER_STATE_SUPPORTED

.. option:: CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED:
.. _CONFIG_SYS_POWER_LOW_POWER_STATE_SUPPORTED:

This option signifies that the target supports the SYS_POWER_LOW_POWER_STATE
configuration option.



:Symbol:           SYS_POWER_LOW_POWER_STATE_SUPPORTED
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
 SOC_QUARK_SE_C1000_SS || SOC_SERIES_QUARK_SE || SOC_SERIES_QUARK_X1000 || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 || SOC_SERIES_KINETIS_K6X || SOC_SERIES_NRF51X || SOC_SERIES_NRF52X || SOC_SERIES_STM32F4X || SOC_SERIES_STM32F1X || SOC_ATMEL_SAM3X8E (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/Kconfig:46