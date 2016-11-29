:orphan:

.. title:: KERNEL_EVENT_LOGGER

.. option:: CONFIG_KERNEL_EVENT_LOGGER:
.. _CONFIG_KERNEL_EVENT_LOGGER:

This feature enables the usage of the profiling logger. Provides the
logging of sleep events (either entering or leaving low power conditions),
context switch events, interrupt events, boot events and a method to
collect these event messages.



:Symbol:           KERNEL_EVENT_LOGGER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable kernel event logger features"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_RING_BUFFER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:86