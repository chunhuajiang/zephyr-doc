:orphan:

.. title:: CACHE_LINE_SIZE_DETECT

.. option:: CONFIG_CACHE_LINE_SIZE_DETECT:
.. _CONFIG_CACHE_LINE_SIZE_DETECT:

This option enables querying the CPUID register for finding the cache line
size at the expense of taking more memory and code and a slightly increased
boot time.

If the CPU's cache line size is known in advance, disable this option and
manually enter the value for CACHE_LINE_SIZE.



:Symbol:           CACHE_LINE_SIZE_DETECT
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Detect d-cache line size at runtime"
 *  "Detect cache line size at runtime"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/arc/Kconfig:272
 * ../arch/x86/Kconfig:175