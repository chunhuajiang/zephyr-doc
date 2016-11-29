:orphan:

.. title:: KERNEL_EVENT_LOGGER_SLEEP

.. option:: CONFIG_KERNEL_EVENT_LOGGER_SLEEP:
.. _CONFIG_KERNEL_EVENT_LOGGER_SLEEP:

Enable low power condition event messages. These messages provide the
following information:

        - When the CPU went to sleep mode.
        - When the CPU woke up.
        - The ID of the interrupt that woke the CPU up.


:Symbol:           KERNEL_EVENT_LOGGER_SLEEP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Sleep event logging point" if KERNEL_EVENT_LOGGER && (MICROKERNEL && SYS_POWER_MANAGEMENT || NANOKERNEL) (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: KERNEL_EVENT_LOGGER && (MICROKERNEL && SYS_POWER_MANAGEMENT || NANOKERNEL) (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 KERNEL_EVENT_LOGGER (value: "n")
:Locations:
 * ../kernel/Kconfig:187