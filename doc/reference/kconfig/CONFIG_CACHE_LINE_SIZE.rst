:orphan:

.. title:: CACHE_LINE_SIZE

.. option:: CONFIG_CACHE_LINE_SIZE:
.. _CONFIG_CACHE_LINE_SIZE:

Size in bytes of a CPU cache line.

Detect automatically at runtime by selecting CACHE_LINE_SIZE_DETECT.



:Symbol:           CACHE_LINE_SIZE
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Cache line size" if !CACHE_LINE_SIZE_DETECT (value: "n")
 *  "Cache line size" if !CACHE_LINE_SIZE_DETECT (value: "n")
:Default values:

 *  32 (value: "n")
 *   Condition: (none)
 *  0 (value: "n")
 *   Condition: CACHE_LINE_SIZE_DETECT (value: "y")
 *  64 (value: "n")
 *   Condition: CPU_ATOM (value: "n")
 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/arc/Kconfig:284
 * ../arch/x86/Kconfig:187