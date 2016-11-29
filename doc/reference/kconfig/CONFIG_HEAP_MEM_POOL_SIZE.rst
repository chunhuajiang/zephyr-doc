:orphan:

.. title:: HEAP_MEM_POOL_SIZE

.. option:: CONFIG_HEAP_MEM_POOL_SIZE:
.. _CONFIG_HEAP_MEM_POOL_SIZE:

This option specifies the size of the heap memory pool used when
dynamically allocating memory using k_malloc(). Supported values
are: 256, 1024, 4096, and 16384. A size of zero means that no
heap memory pool is defined.



:Symbol:           HEAP_MEM_POOL_SIZE
:Type:             int
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Heap memory pool size (in bytes)"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:346