:orphan:

.. title:: UART_DRV_CMD

.. option:: CONFIG_UART_DRV_CMD:
.. _CONFIG_UART_DRV_CMD:

This enables the API to send extra commands to drivers.
This allows drivers to expose hardware specific functions.

Says no if not sure.



:Symbol:           UART_DRV_CMD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable driver commands API"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SERIAL (value: "n")
:Locations:
 * ../drivers/serial/Kconfig:57