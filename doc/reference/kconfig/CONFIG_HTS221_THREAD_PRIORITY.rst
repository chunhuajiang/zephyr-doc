:orphan:

.. title:: HTS221_THREAD_PRIORITY

.. option:: CONFIG_HTS221_THREAD_PRIORITY:
.. _CONFIG_HTS221_THREAD_PRIORITY:

Priority of thread used by the driver to handle interrupts.



:Symbol:           HTS221_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if HTS221 && HTS221_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: HTS221 && HTS221_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:89