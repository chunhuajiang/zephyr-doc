:orphan:

.. title:: CLOCK_CONTROL_QUARK_SE_PERIPHERAL

.. option:: CONFIG_CLOCK_CONTROL_QUARK_SE_PERIPHERAL:
.. _CONFIG_CLOCK_CONTROL_QUARK_SE_PERIPHERAL:

Enable support for Quark SE peripheral clock which controls the
clock of I2C, SPI, GPIO controllers and more.



:Symbol:           CLOCK_CONTROL_QUARK_SE_PERIPHERAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE peripheral clock support" if CLOCK_CONTROL && CLOCK_CONTROL_QUARK_SE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CLOCK_CONTROL && CLOCK_CONTROL_QUARK_SE (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL && SOC_SERIES_QUARK_SE && CLOCK_CONTROL_QUARK_SE (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.quark_se:29
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:123