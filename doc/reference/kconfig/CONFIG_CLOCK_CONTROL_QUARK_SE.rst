:orphan:

.. title:: CLOCK_CONTROL_QUARK_SE

.. option:: CONFIG_CLOCK_CONTROL_QUARK_SE:
.. _CONFIG_CLOCK_CONTROL_QUARK_SE:

Enable support for the Quark SE clock driver.



:Symbol:           CLOCK_CONTROL_QUARK_SE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE Clock controller support" if CLOCK_CONTROL && SOC_QUARK_SE_C1000 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CLOCK_CONTROL && SOC_QUARK_SE_C1000 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.quark_se:21
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:118