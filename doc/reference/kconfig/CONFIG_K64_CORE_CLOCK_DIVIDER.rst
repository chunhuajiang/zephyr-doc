:orphan:

.. title:: K64_CORE_CLOCK_DIVIDER

.. option:: CONFIG_K64_CORE_CLOCK_DIVIDER:
.. _CONFIG_K64_CORE_CLOCK_DIVIDER:

This option specifies the divide value for the K64 processor core clock
from the system clock.



:Symbol:           K64_CORE_CLOCK_DIVIDER
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64 core clock divider"
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_KINETIS_K6X && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.soc:77