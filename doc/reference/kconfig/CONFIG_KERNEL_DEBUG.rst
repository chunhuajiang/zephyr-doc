:orphan:

.. title:: KERNEL_DEBUG

.. option:: CONFIG_KERNEL_DEBUG:
.. _CONFIG_KERNEL_DEBUG:

Enable kernel debugging.

Note that debugging the kernel internals can be very verbose.



:Symbol:           KERNEL_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kernel debugging"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_INIT_STACKS`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:21