:orphan:

.. title:: I2C_KSDK

.. option:: CONFIG_I2C_KSDK:
.. _CONFIG_I2C_KSDK:

Enable the ksdk I2C driver.



:Symbol:           I2C_KSDK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "KSDK I2C driver" if I2C && HAS_KSDK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: I2C && HAS_KSDK (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && I2C (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:68
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:44