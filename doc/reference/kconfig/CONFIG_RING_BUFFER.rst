:orphan:

.. title:: RING_BUFFER

.. option:: CONFIG_RING_BUFFER:
.. _CONFIG_RING_BUFFER:

Enable usage of ring buffers. Similar to nanokernel FIFOs but manage
their own buffer memory and can store arbitrary data. For optimal
performance, use buffer sizes that are a power of 2.



:Symbol:           RING_BUFFER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable ring buffers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 KERNEL_EVENT_LOGGER || IPM_CONSOLE_RECEIVER && CONSOLE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/Kconfig:77