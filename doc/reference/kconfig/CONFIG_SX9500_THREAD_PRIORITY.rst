:orphan:

.. title:: SX9500_THREAD_PRIORITY

.. option:: CONFIG_SX9500_THREAD_PRIORITY:
.. _CONFIG_SX9500_THREAD_PRIORITY:

The configuration item CONFIG_SX9500_THREAD_PRIORITY:

:Symbol:           SX9500_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if SX9500 && SX9500_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: SX9500 && SX9500_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:97