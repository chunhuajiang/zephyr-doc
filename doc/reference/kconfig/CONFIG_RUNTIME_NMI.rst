:orphan:

.. title:: RUNTIME_NMI

.. option:: CONFIG_RUNTIME_NMI:
.. _CONFIG_RUNTIME_NMI:

The kernel provides a simple NMI handler that simply hangs in a tight
loop if triggered. This fills the requirement that there must be an
NMI handler installed when the CPU boots. If a custom handler is
needed, enable this option and attach it via _NmiHandlerSet().



:Symbol:           RUNTIME_NMI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Attach an NMI handler at runtime"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_REBOOT`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M (value: "n")
:Locations:
 * ../arch/arm/core/cortex_m/Kconfig:135