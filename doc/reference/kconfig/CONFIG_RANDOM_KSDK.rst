:orphan:

.. title:: RANDOM_KSDK

.. option:: CONFIG_RANDOM_KSDK:
.. _CONFIG_RANDOM_KSDK:

This option enables the random number generator accelerator (RNGA)
driver based on the KSDK RNGA driver.



:Symbol:           RANDOM_KSDK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "KSDK Random driver" if RANDOM_GENERATOR && HAS_RNGA (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: RANDOM_GENERATOR && HAS_RNGA (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && RANDOM_GENERATOR (value: "n")
:Locations:
 * ../drivers/random/Kconfig:59
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:75