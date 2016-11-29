:orphan:

.. title:: UART_STELLARIS_PORT_1

.. option:: CONFIG_UART_STELLARIS_PORT_1:
.. _CONFIG_UART_STELLARIS_PORT_1:

This tells the driver to configure the UART port at boot, depending on
the additional configure options below.



:Symbol:           UART_STELLARIS_PORT_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Stellaris UART Port 1" if UART_STELLARIS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: UART_STELLARIS (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 UART_STELLARIS && SOC_TI_LM3S6965 (value: "n")
:Locations:
 * ../drivers/serial/Kconfig.stellaris:46
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:56