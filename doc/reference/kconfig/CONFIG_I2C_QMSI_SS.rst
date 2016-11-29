:orphan:

.. title:: I2C_QMSI_SS

.. option:: CONFIG_I2C_QMSI_SS:
.. _CONFIG_I2C_QMSI_SS:

This option enable the Sensor QMSI I2C driver.

This driver is simply a shim driver based on the I2C driver
provided by the QMSI BSP.



:Symbol:           I2C_QMSI_SS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI I2C driver for the Sensor Subsystem" if I2C && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C && QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_QUARK_SE_C1000_SS (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:38
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:144