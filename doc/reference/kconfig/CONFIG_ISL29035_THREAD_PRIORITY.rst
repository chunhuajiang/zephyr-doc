:orphan:

.. title:: ISL29035_THREAD_PRIORITY

.. option:: CONFIG_ISL29035_THREAD_PRIORITY:
.. _CONFIG_ISL29035_THREAD_PRIORITY:

Priority of thread used by the driver to handle interrupts.



:Symbol:           ISL29035_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if ISL29035 (value: "n")
 *  "Thread priority" if ISL29035 && ISL29035_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: ISL29035 (value: "n")
 *  10 (value: "n")
 *   Condition: ISL29035 && ISL29035_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:44
 * ../drivers/sensor/isl29035/Kconfig:174