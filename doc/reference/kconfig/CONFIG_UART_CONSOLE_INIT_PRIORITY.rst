:orphan:

.. title:: UART_CONSOLE_INIT_PRIORITY

.. option:: CONFIG_UART_CONSOLE_INIT_PRIORITY:
.. _CONFIG_UART_CONSOLE_INIT_PRIORITY:

Device driver initialization priority.
Console has to be initialized after the UART driver
it uses.



:Symbol:           UART_CONSOLE_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if UART_CONSOLE (value: "n")
:Default values:

 *  60 (value: "n")
 *   Condition: UART_CONSOLE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:76