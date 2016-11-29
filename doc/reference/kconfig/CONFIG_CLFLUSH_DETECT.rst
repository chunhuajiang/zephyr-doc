:orphan:

.. title:: CLFLUSH_DETECT

.. option:: CONFIG_CLFLUSH_DETECT:
.. _CONFIG_CLFLUSH_DETECT:

This option should be enabled if it is not known in advance whether the
CPU supports the CLFLUSH instruction or not.

The CPU is queried at boot time to determine which of the multiple
implementations of sys_cache_flush() linked into the image is the
correct one to use.

If the CPU's support (or lack thereof) of CLFLUSH is known in advance, then
disable this option and set CLFLUSH_INSTRUCTION_SUPPORTED as appropriate.



:Symbol:           CLFLUSH_DETECT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Detect support of CLFLUSH instruction at runtime" if CACHE_FLUSHING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CACHE_FLUSHING (value: "n")
 *  y (value: "y")
 *   Condition: CACHE_FLUSHING (value: "n")
 *  y (value: "y")
 *   Condition: CACHE_FLUSHING (value: "n")
 *  y (value: "y")
 *   Condition: CACHE_FLUSHING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_ATOM (value: "n")
:Locations:
 * ../arch/x86/Kconfig:211
 * ../arch/x86/soc/ia32/Kconfig.defconfig:41
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:40
 * ../arch/x86/soc/atom/Kconfig.defconfig:41