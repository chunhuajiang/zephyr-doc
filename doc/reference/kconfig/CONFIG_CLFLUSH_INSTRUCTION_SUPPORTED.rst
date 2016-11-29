:orphan:

.. title:: CLFLUSH_INSTRUCTION_SUPPORTED

.. option:: CONFIG_CLFLUSH_INSTRUCTION_SUPPORTED:
.. _CONFIG_CLFLUSH_INSTRUCTION_SUPPORTED:

An implementation of sys_cache_flush() that uses CLFLUSH is made
available, instead of the one using WBINVD.

This option should only be enabled if it is known in advance that the
CPU supports the CLFLUSH instruction. It disables runtime detection of
CLFLUSH support thereby reducing both memory footprint and boot time.



:Symbol:           CLFLUSH_INSTRUCTION_SUPPORTED
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "CLFLUSH instruction supported" if !CLFLUSH_DETECT && CACHE_FLUSHING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: !CLFLUSH_DETECT && CACHE_FLUSHING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:198