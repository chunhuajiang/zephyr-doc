:orphan:

.. title:: CLOCK_CONTROL_QUARK_SE_SENSOR_DRV_NAME

.. option:: CONFIG_CLOCK_CONTROL_QUARK_SE_SENSOR_DRV_NAME:
.. _CONFIG_CLOCK_CONTROL_QUARK_SE_SENSOR_DRV_NAME:

The configuration item CONFIG_CLOCK_CONTROL_QUARK_SE_SENSOR_DRV_NAME:

:Symbol:           CLOCK_CONTROL_QUARK_SE_SENSOR_DRV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE sensor clock device name" if CLOCK_CONTROL_QUARK_SE_SENSOR (value: "n")
:Default values:

 *  "clk_sensor"
 *   Condition: CLOCK_CONTROL_QUARK_SE_SENSOR (value: "n")
 *  "clk_sensor"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CLOCK_CONTROL && SOC_SERIES_QUARK_SE && CLOCK_CONTROL_QUARK_SE (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.quark_se:66
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:135