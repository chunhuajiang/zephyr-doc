:orphan:

.. title:: UART_NSIM

.. option:: CONFIG_UART_NSIM:
.. _CONFIG_UART_NSIM:

This enables the UART driver for the MetaWare nSim simulator.



:Symbol:           UART_NSIM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "UART driver for MetaWare nSim" if NSIM && SERIAL (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NSIM && SERIAL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.nsim:1