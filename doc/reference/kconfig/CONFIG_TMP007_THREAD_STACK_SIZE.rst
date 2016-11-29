:orphan:

.. title:: TMP007_THREAD_STACK_SIZE

.. option:: CONFIG_TMP007_THREAD_STACK_SIZE:
.. _CONFIG_TMP007_THREAD_STACK_SIZE:

Stack size of thread used by the driver to handle interrupts.


:Symbol:           TMP007_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if TMP007 && TMP007_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: TMP007 && TMP007_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:116