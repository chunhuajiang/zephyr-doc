:orphan:

.. title:: ETH_ENC28J60_0_GPIO_PORT_NAME

.. option:: CONFIG_ETH_ENC28J60_0_GPIO_PORT_NAME:
.. _CONFIG_ETH_ENC28J60_0_GPIO_PORT_NAME:

GPIO port name through which ENC28J60C interruption is received.



:Symbol:           ETH_ENC28J60_0_GPIO_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO controller port name"
:Default values:

 *  "GPIO_0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ETH_ENC28J60 && ETH_ENC28J60_0 (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.enc28j60:56