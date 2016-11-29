:orphan:

.. title:: CLOCK_CONTROL_NRF5_K32SRC_DRV_NAME

.. option:: CONFIG_CLOCK_CONTROL_NRF5_K32SRC_DRV_NAME:
.. _CONFIG_CLOCK_CONTROL_NRF5_K32SRC_DRV_NAME:

The configuration item CONFIG_CLOCK_CONTROL_NRF5_K32SRC_DRV_NAME:

:Symbol:           CLOCK_CONTROL_NRF5_K32SRC_DRV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NRF5 32KHz clock device name" if CLOCK_CONTROL_NRF5 (value: "n")
:Default values:

 *  "clk_k32src"
 *   Condition: CLOCK_CONTROL_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.nrf5:41