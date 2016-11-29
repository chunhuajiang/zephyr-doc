:orphan:

.. title:: I2C_ATMEL_SAM3

.. option:: CONFIG_I2C_ATMEL_SAM3:
.. _CONFIG_I2C_ATMEL_SAM3:

Enable I2C support on the Atmel SAM3 family processor.

Says y to enable additional options to enable support
for individual controllers.



:Symbol:           I2C_ATMEL_SAM3
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 I2C Driver" if I2C && SOC_ATMEL_SAM3 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C && SOC_ATMEL_SAM3 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C && BOARD_ARDUINO_DUE (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:58
 * ../arch/arm/soc/atmel_sam3/Kconfig.defconfig:99
 * ../boards/arm/arduino_due/Kconfig.defconfig:9