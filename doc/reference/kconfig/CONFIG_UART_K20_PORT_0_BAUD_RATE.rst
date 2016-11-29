:orphan:

.. title:: UART_K20_PORT_0_BAUD_RATE

.. option:: CONFIG_UART_K20_PORT_0_BAUD_RATE:
.. _CONFIG_UART_K20_PORT_0_BAUD_RATE:

The baud rate for UART port to be set to at boot.

Leave at 0 to skip initialization.



:Symbol:           UART_K20_PORT_0_BAUD_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Port 0 Baud Rate" if UART_K20_PORT_0 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: UART_K20_PORT_0 (value: "n")
 *  115200 (value: "n")
 *   Condition: (none)
 *  115200 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_K20 && BOARD_FRDM_K64F && UART_K20_PORT_0 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.k20:35
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:48
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:48