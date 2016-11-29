:orphan:

.. title:: I2C_0_IRQ_SHARED_NAME

.. option:: CONFIG_I2C_0_IRQ_SHARED_NAME:
.. _CONFIG_I2C_0_IRQ_SHARED_NAME:

Specify the device name for the shared IRQ driver. It is used to register
this driver with the shared IRQ driver, so interrupts can be dispatched
correctly.



:Symbol:           I2C_0_IRQ_SHARED_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Shared IRQ" if I2C_0 && I2C_0_IRQ_SHARED (value: "n")
:Default values:

 *  SHARED_IRQ_0_NAME (value: "")
 *   Condition: SHARED_IRQ (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && SOC_SERIES_QUARK_X1000 && I2C_DW && I2C_0 (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:133
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:95