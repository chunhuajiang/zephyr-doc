:orphan:

.. title:: I2C

.. option:: CONFIG_I2C:
.. _CONFIG_I2C:

Enable I2C Driver Configuration



:Symbol:           I2C
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Drivers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:22
 * ../boards/x86/galileo/Kconfig.defconfig:10