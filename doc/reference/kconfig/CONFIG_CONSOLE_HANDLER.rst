:orphan:

.. title:: CONSOLE_HANDLER

.. option:: CONFIG_CONSOLE_HANDLER:
.. _CONFIG_CONSOLE_HANDLER:

This option enables console input handler allowing to write simple
interaction between serial console and the OS.



:Symbol:           CONSOLE_HANDLER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable console input handler" if UART_CONSOLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_CONSOLE (value: "n")
:Selects:

 *  :option:`CONFIG_UART_INTERRUPT_DRIVEN` if UART_CONSOLE (value: "n")
:Reverse (select-related) dependencies:
 GDB_SERVER_INTERRUPT_DRIVEN && GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:32