:orphan:

.. title:: UART_STELLARIS_PORT_2

.. option:: CONFIG_UART_STELLARIS_PORT_2:
.. _CONFIG_UART_STELLARIS_PORT_2:

This tells the driver to configure the UART port at boot, depending on
the additional configure options below.



:Symbol:           UART_STELLARIS_PORT_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Stellaris UART Port 2" if UART_STELLARIS (value: "n")
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
 * ../drivers/serial/Kconfig.stellaris:80
 * ../arch/arm/soc/ti_lm3s6965/Kconfig.defconfig:66