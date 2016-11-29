:orphan:

.. title:: SHT3XD_THREAD_STACK_SIZE

.. option:: CONFIG_SHT3XD_THREAD_STACK_SIZE:
.. _CONFIG_SHT3XD_THREAD_STACK_SIZE:

Stack size of thread used by the driver to handle interrupts.



:Symbol:           SHT3XD_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if SHT3XD && SHT3XD_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: SHT3XD && SHT3XD_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:109