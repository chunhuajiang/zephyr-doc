:orphan:

.. title:: KERNEL_EVENT_LOGGER_BUFFER_SIZE

.. option:: CONFIG_KERNEL_EVENT_LOGGER_BUFFER_SIZE:
.. _CONFIG_KERNEL_EVENT_LOGGER_BUFFER_SIZE:

Buffer size in 32-bit words.



:Symbol:           KERNEL_EVENT_LOGGER_BUFFER_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kernel event logger buffer size" if KERNEL_EVENT_LOGGER (value: "n")
:Default values:

 *  128 (value: "n")
 *   Condition: KERNEL_EVENT_LOGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:97