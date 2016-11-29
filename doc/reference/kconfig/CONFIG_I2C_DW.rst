:orphan:

.. title:: I2C_DW

.. option:: CONFIG_I2C_DW:
.. _CONFIG_I2C_DW:

Enable Design Ware I2C support on the selected board



:Symbol:           I2C_DW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Design Ware I2C support" if I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:31
 * ../arch/arc/soc/em11d/Kconfig.defconfig:139
 * ../arch/arc/soc/em7d/Kconfig.defconfig:139
 * ../arch/arc/soc/em9d/Kconfig.defconfig:137
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:79