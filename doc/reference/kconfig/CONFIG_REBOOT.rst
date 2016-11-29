:orphan:

.. title:: REBOOT

.. option:: CONFIG_REBOOT:
.. _CONFIG_REBOOT:

Enable the sys_reboot() API. Enabling this can drag in other subsystems
needed to perform a "safe" reboot (e.g. SYSTEM_CLOCK_DISABLE, to stop the
system clock before issuing a reset).


:Symbol:           REBOOT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Reboot functionality"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_SYSTEM_CLOCK_DISABLE`
:Reverse (select-related) dependencies:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M && RUNTIME_NMI || GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:410