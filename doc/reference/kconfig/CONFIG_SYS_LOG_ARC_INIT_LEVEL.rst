:orphan:

.. title:: SYS_LOG_ARC_INIT_LEVEL

.. option:: CONFIG_SYS_LOG_ARC_INIT_LEVEL:
.. _CONFIG_SYS_LOG_ARC_INIT_LEVEL:

Sets log level for the boot initialization and boot process of the sensor
sub-system.

Levels are:

- 0 OFF, do not write

- 1 ERROR, only write SYS_LOG_ERR

- 2 WARNING, write SYS_LOG_WRN in adition to previous level

- 3 INFO, write SYS_LOG_INF in adition to previous levels

- 4 DEBUG, write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_ARC_INIT_LEVEL
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Quark SE Sensor Subsystem log level"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:41