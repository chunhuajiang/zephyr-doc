:orphan:

.. title:: KERNEL_EVENT_LOGGER_DYNAMIC

.. option:: CONFIG_KERNEL_EVENT_LOGGER_DYNAMIC:
.. _CONFIG_KERNEL_EVENT_LOGGER_DYNAMIC:

If enabled, kernel event logger is not logging any data to the ring buffer
It is up to the application to set the appropriate flags to enable/disable the
logging of each event type.



:Symbol:           KERNEL_EVENT_LOGGER_DYNAMIC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kernel event logger dynamic enabling" if KERNEL_EVENT_LOGGER (value: "n")
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
 * ../kernel/Kconfig:105