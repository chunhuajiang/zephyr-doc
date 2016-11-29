:orphan:

.. title:: MAIN_STACK_SIZE

.. option:: CONFIG_MAIN_STACK_SIZE:
.. _CONFIG_MAIN_STACK_SIZE:

When the intitialization is complete, the thread executing it then
executes the main() routine, so as to reuse the stack used by the
initialization, which would be wasted RAM otherwise.

After initialization is complete, the thread runs main().



:Symbol:           MAIN_STACK_SIZE
:Type:             int
:Value:            "1024"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Size of stack for initialization and main thread"
:Default values:

 *  1024 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:122