:orphan:

.. title:: WDOG_INIT

.. option:: CONFIG_WDOG_INIT:
.. _CONFIG_WDOG_INIT:

This processor enables the watchdog timer with a short timeout
upon reset. Therefore, this requires that the watchdog be configured
during reset handling.



:Symbol:           WDOG_INIT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_KINETIS_K6X && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.soc:109