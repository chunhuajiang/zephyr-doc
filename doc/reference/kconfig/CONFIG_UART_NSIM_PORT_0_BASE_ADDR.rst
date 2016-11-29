:orphan:

.. title:: UART_NSIM_PORT_0_BASE_ADDR

.. option:: CONFIG_UART_NSIM_PORT_0_BASE_ADDR:
.. _CONFIG_UART_NSIM_PORT_0_BASE_ADDR:

The base address of UART port.

Leave this at 0x00000000 to skip initialization at boot.


:Symbol:           UART_NSIM_PORT_0_BASE_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Register Address" if UART_NSIM (value: "n")
:Default values:

 *  0x00000000 (value: "n")
 *   Condition: UART_NSIM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nsim:16