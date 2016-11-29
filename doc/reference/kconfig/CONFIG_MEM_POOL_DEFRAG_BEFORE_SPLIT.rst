:orphan:

.. title:: MEM_POOL_DEFRAG_BEFORE_SPLIT

.. option:: CONFIG_MEM_POOL_DEFRAG_BEFORE_SPLIT:
.. _CONFIG_MEM_POOL_DEFRAG_BEFORE_SPLIT:

This option instructs a memory pool to try merging smaller unused
blocks if an unused block of the required size is not available; only
if this does not generate a sufficiently large block will the memory
pool try splitting a larger unused block. This policy attempts to
preserve the memory pool's larger blocks, at the cost of performing
automatic partial defragmentations more frequently.



:Symbol:           MEM_POOL_DEFRAG_BEFORE_SPLIT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Merge smaller blocks before splitting a larger block"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:321