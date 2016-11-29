:orphan:

.. title:: ARCH_CACHE_FLUSH_DETECT

.. option:: CONFIG_ARCH_CACHE_FLUSH_DETECT:
.. _CONFIG_ARCH_CACHE_FLUSH_DETECT:

The configuration item CONFIG_ARCH_CACHE_FLUSH_DETECT:

:Symbol:           ARCH_CACHE_FLUSH_DETECT
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
 *  y (value: "y")
 *   Condition: CLFLUSH_DETECT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/arc/Kconfig:293
 * ../arch/x86/Kconfig:227