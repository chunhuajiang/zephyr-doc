:orphan:

.. title:: MEM_SAFE_CHECK_BOUNDARIES

.. option:: CONFIG_MEM_SAFE_CHECK_BOUNDARIES:
.. _CONFIG_MEM_SAFE_CHECK_BOUNDARIES:

This implementation checks the application image's text/rodata
boundaries for its read-only region and the data/bss/noinit boundaries
for its read-write region, in software.

Other regions can be added as needed by using the
sys_mem_safe_region_add() API. The number of regions that can be added
is controlled via the MEM_SAFE_NUM_REGIONS kconfig option.

This implementation requires initialization and thus consumes some boot
time.



:Symbol:           MEM_SAFE_CHECK_BOUNDARIES
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Software validation of memory access within memory regions"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:36