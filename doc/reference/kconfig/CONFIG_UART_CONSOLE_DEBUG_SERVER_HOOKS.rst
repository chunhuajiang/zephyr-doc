:orphan:

.. title:: UART_CONSOLE_DEBUG_SERVER_HOOKS

.. option:: CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS:
.. _CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS:

This option allows a debug server agent such as GDB to take over the
handling of traffic that goes through the console logic. The debug
server looks at characters received and decides to handle them itself if
they are some sort of control characters, or let the regular console
code handle them if they are of no special significance to it.



:Symbol:           UART_CONSOLE_DEBUG_SERVER_HOOKS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug server hooks in debug console" if UART_CONSOLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_CONSOLE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 GDB_SERVER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:86