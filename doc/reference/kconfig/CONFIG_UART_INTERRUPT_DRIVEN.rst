:orphan:

.. title:: UART_INTERRUPT_DRIVEN

.. option:: CONFIG_UART_INTERRUPT_DRIVEN:
.. _CONFIG_UART_INTERRUPT_DRIVEN:

This option enables interrupt support for UART allowing console
input and other UART based drivers.



:Symbol:           UART_INTERRUPT_DRIVEN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable UART Interrupt support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H4 || BLUETOOTH_HCI && BLUETOOTH && !BLUETOOTH_CONTROLLER && SERIAL && BLUETOOTH_H5 || BLUETOOTH_CUSTOM && BLUETOOTH && SERIAL && NBLE || UART_CONSOLE && CONSOLE && CONSOLE_HANDLER || UART_PIPE && CONSOLE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 SERIAL && BOARD_V2M_BEETLE (value: "n")
:Locations:
 * ../drivers/serial/Kconfig:38
 * ../boards/arm/v2m_beetle/Kconfig.defconfig:68