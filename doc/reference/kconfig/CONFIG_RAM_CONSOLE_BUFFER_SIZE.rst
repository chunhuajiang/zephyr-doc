:orphan:

.. title:: RAM_CONSOLE_BUFFER_SIZE

.. option:: CONFIG_RAM_CONSOLE_BUFFER_SIZE:
.. _CONFIG_RAM_CONSOLE_BUFFER_SIZE:

Size of the RAM console buffer. Messages will wrap around if the
length is exceeded.



:Symbol:           RAM_CONSOLE_BUFFER_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Ram Console buffer size" if RAM_CONSOLE (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: RAM_CONSOLE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:122