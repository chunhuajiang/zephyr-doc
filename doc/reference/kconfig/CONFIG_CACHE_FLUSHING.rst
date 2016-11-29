:orphan:

.. title:: CACHE_FLUSHING

.. option:: CONFIG_CACHE_FLUSHING:
.. _CONFIG_CACHE_FLUSHING:

This links in the sys_cache_flush() function. A mechanism for flushing the
cache must be selected as well. By default, that mechanism is discovered at
runtime.


:Symbol:           CACHE_FLUSHING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable d-cache flushing mechanism"
 *  "Enable cache flushing mechanism"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 SOC_EM7D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:297
 * ../arch/x86/Kconfig:232
 * ../arch/arc/soc/em11d/Kconfig.defconfig:68
 * ../arch/arc/soc/em7d/Kconfig.defconfig:68