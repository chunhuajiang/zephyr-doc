:orphan:

.. title:: BOOTLOADER_CONTEXT_RESTORE_SUPPORTED

.. option:: CONFIG_BOOTLOADER_CONTEXT_RESTORE_SUPPORTED:
.. _CONFIG_BOOTLOADER_CONTEXT_RESTORE_SUPPORTED:

This option signifies that the target has options of bootloaders
that support context restore upon resume from deep sleep



:Symbol:           BOOTLOADER_CONTEXT_RESTORE_SUPPORTED
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
 SOC_SERIES_QUARK_SE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../arch/Kconfig:62