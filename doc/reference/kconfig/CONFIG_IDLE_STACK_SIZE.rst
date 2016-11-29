:orphan:

.. title:: IDLE_STACK_SIZE

.. option:: CONFIG_IDLE_STACK_SIZE:
.. _CONFIG_IDLE_STACK_SIZE:

Depending on the work that the idle task must do, most likely due to
power management but possibly to other features like system event
logging (e.g. logging when the system goes to sleep), the idle thread
may need more stack space than the default value.



:Symbol:           IDLE_STACK_SIZE
:Type:             int
:Value:            "256"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Size of stack for idle thread"
:Default values:

 *  256 (value: "n")
 *   Condition: (none)
 *  320 (value: "n")
 *   Condition: ARC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:133