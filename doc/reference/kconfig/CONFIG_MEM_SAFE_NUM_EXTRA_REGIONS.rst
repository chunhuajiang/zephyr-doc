:orphan:

.. title:: MEM_SAFE_NUM_EXTRA_REGIONS

.. option:: CONFIG_MEM_SAFE_NUM_EXTRA_REGIONS:
.. _CONFIG_MEM_SAFE_NUM_EXTRA_REGIONS:

The functions available in mem_safe.h check if memory is within
read-only or read-write regions before accessing it instead of crashing.
The kernel image is added as a valid region automatically, but other
regions can be added if the application makes access to additional
memory outside of the image's boundaries.



:Symbol:           MEM_SAFE_NUM_EXTRA_REGIONS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of safe memory access regions to be added at runtime" if MEM_SAFE_CHECK_BOUNDARIES (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: MEM_SAFE_CHECK_BOUNDARIES (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:53