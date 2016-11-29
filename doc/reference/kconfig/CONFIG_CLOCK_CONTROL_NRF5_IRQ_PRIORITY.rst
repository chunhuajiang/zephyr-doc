:orphan:

.. title:: CLOCK_CONTROL_NRF5_IRQ_PRIORITY

.. option:: CONFIG_CLOCK_CONTROL_NRF5_IRQ_PRIORITY:
.. _CONFIG_CLOCK_CONTROL_NRF5_IRQ_PRIORITY:

The interrupt priority for Power Clock interrupt.



:Symbol:           CLOCK_CONTROL_NRF5_IRQ_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 7]
:Prompts:

 *  "Power Clock Interrupt Priority" if CLOCK_CONTROL_NRF5 (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: CLOCK_CONTROL_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.nrf5:26