:orphan:

.. title:: KERNEL_EVENT_LOGGER_CONTEXT_SWITCH

.. option:: CONFIG_KERNEL_EVENT_LOGGER_CONTEXT_SWITCH:
.. _CONFIG_KERNEL_EVENT_LOGGER_CONTEXT_SWITCH:

Enable the context switch event messages.



:Symbol:           KERNEL_EVENT_LOGGER_CONTEXT_SWITCH
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Context switch event logging point" if KERNEL_EVENT_LOGGER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: KERNEL_EVENT_LOGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 KERNEL_EVENT_LOGGER (value: "n")
:Locations:
 * ../kernel/Kconfig:170