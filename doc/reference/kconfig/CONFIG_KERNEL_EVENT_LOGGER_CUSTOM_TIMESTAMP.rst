:orphan:

.. title:: KERNEL_EVENT_LOGGER_CUSTOM_TIMESTAMP

.. option:: CONFIG_KERNEL_EVENT_LOGGER_CUSTOM_TIMESTAMP:
.. _CONFIG_KERNEL_EVENT_LOGGER_CUSTOM_TIMESTAMP:

This flag enables the possibility to set the timer function to be used to
populate kernel event logger timestamp. This has to be done at runtime by
calling sys_k_event_logger_set_timer and providing the function callback.



:Symbol:           KERNEL_EVENT_LOGGER_CUSTOM_TIMESTAMP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kernel event logger custom timestamp" if KERNEL_EVENT_LOGGER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: KERNEL_EVENT_LOGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:115