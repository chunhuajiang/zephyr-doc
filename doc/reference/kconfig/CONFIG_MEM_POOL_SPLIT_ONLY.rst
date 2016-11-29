:orphan:

.. title:: MEM_POOL_SPLIT_ONLY

.. option:: CONFIG_MEM_POOL_SPLIT_ONLY:
.. _CONFIG_MEM_POOL_SPLIT_ONLY:

This option instructs a memory pool to try splitting a larger unused
block if an unused block of the required size is not available; if no
such blocks exist the block allocation operation fails. This policy
attempts to limit the cost of defragmenting the memory pool by avoiding
automatic partial defragmentation, at the cost of requiring the
application to explicitly request a full defragmentation of the memory
pool when an allocation fails. Depending on how a memory pool is used,
it may be more efficient for a memory pool to perform an occasional
full defragmentation than to perform frequent partial defragmentations.



:Symbol:           MEM_POOL_SPLIT_ONLY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Split a larger block, but never merge smaller blocks"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:331