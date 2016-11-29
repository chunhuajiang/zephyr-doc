:orphan:

.. title:: MEM_POOL_SPLIT_BEFORE_DEFRAG

.. option:: CONFIG_MEM_POOL_SPLIT_BEFORE_DEFRAG:
.. _CONFIG_MEM_POOL_SPLIT_BEFORE_DEFRAG:

This option instructs a memory pool to try splitting a larger unused
block if an unused block of the required size is not available; only
if no such blocks exist will the memory pool try merging smaller unused
blocks. This policy attempts to limit the cost of performing automatic
partial defragmention of the memory pool, at the cost of fragmenting
the memory pool's larger blocks.



:Symbol:           MEM_POOL_SPLIT_BEFORE_DEFRAG
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Split a larger block before merging smaller blocks"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:311