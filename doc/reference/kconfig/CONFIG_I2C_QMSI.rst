:orphan:

.. title:: I2C_QMSI

.. option:: CONFIG_I2C_QMSI:
.. _CONFIG_I2C_QMSI:

This option enable the QMSI I2C driver.

This driver is simply a shim driver based on the I2C driver
provided by the QMSI BSP.



:Symbol:           I2C_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI I2C driver" if I2C && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C && QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:48
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:110
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:78