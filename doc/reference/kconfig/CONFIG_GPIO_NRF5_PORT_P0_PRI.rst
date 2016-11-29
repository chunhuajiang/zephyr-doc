:orphan:

.. title:: GPIO_NRF5_PORT_P0_PRI

.. option:: CONFIG_GPIO_NRF5_PORT_P0_PRI:
.. _CONFIG_GPIO_NRF5_PORT_P0_PRI:

nRF5X Port P0 IRQ priority.



:Symbol:           GPIO_NRF5_PORT_P0_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 1] if SOC_SERIES_NRF51X (value: "n")
 *  [0, 5] if SOC_SERIES_NRF52X (value: "n")
:Prompts:

 *  "GPIOTE P0 interrupt priority" if GPIO_NRF5_P0 (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: GPIO_NRF5_P0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_NRF5 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.nrf5:41