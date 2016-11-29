:orphan:

.. title:: ISL29035_THREAD_STACK_SIZE

.. option:: CONFIG_ISL29035_THREAD_STACK_SIZE:
.. _CONFIG_ISL29035_THREAD_STACK_SIZE:

Stack size of thread used by the driver to handle interrupts.



:Symbol:           ISL29035_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if ISL29035 && ISL29035_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: ISL29035 && ISL29035_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:182