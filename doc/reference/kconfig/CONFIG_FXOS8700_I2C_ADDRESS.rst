:orphan:

.. title:: FXOS8700_I2C_ADDRESS

.. option:: CONFIG_FXOS8700_I2C_ADDRESS:
.. _CONFIG_FXOS8700_I2C_ADDRESS:

The I2C slave address can be configured by the SA0 and SA1 input pins.
This option should usually be set by the board defconfig.



:Symbol:           FXOS8700_I2C_ADDRESS
:Type:             hex
:Value:            "0x1c"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0x1c, 0x1f]
:Prompts:

 *  "I2C address" if FXOS8700 (value: "n")
:Default values:

 *  0x1d (value: "n")
 *   Condition: FXOS8700 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/fxos8700/Kconfig:54