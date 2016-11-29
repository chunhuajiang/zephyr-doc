:orphan:

.. title:: BOOTLOADER_CONTEXT_RESTORE

.. option:: CONFIG_BOOTLOADER_CONTEXT_RESTORE:
.. _CONFIG_BOOTLOADER_CONTEXT_RESTORE:

This option signifies that the target has a bootloader
that restores CPU context upon resuming from deep sleep
power state.



:Symbol:           BOOTLOADER_CONTEXT_RESTORE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Boot loader has context restore support" if SYS_POWER_DEEP_SLEEP && BOOTLOADER_CONTEXT_RESTORE_SUPPORTED (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: SYS_POWER_DEEP_SLEEP && BOOTLOADER_CONTEXT_RESTORE_SUPPORTED (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:400