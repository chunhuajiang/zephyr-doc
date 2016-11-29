:orphan:

.. title:: I2C_CLOCK_SPEED

.. option:: CONFIG_I2C_CLOCK_SPEED:
.. _CONFIG_I2C_CLOCK_SPEED:

The configuration item CONFIG_I2C_CLOCK_SPEED:

:Symbol:           I2C_CLOCK_SPEED
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Set the clock speed for I2C" if I2C (value: "n")
:Default values:

 *  32 (value: "n")
 *   Condition: I2C (value: "n")
 *  100 (value: "n")
 *   Condition: (none)
 *  100 (value: "n")
 *   Condition: (none)
 *  100 (value: "n")
 *   Condition: (none)
 *  25 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:83
 * ../arch/arc/soc/em11d/Kconfig.defconfig:136
 * ../arch/arc/soc/em7d/Kconfig.defconfig:136
 * ../arch/arc/soc/em9d/Kconfig.defconfig:134
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:76