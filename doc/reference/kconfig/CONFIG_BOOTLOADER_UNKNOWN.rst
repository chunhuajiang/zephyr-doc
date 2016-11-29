:orphan:

.. title:: BOOTLOADER_UNKNOWN

.. option:: CONFIG_BOOTLOADER_UNKNOWN:
.. _CONFIG_BOOTLOADER_UNKNOWN:

This option signifies that the target has a generic bootloader
or that it supports multiple ways of booting and it isn't clear
at build time which method is to be used. When this option is enabled
the board may have to do extra work to ensure a proper startup.



:Symbol:           BOOTLOADER_UNKNOWN
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Generic boot loader support" if X86 (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: X86 (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_IA32 || SOC_SERIES_QUARK_X1000 || SOC_ATOM || SOC_SERIES_QUARK_X1000 && X86 && SOC_QUARK_X1000 (value: "y")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:389