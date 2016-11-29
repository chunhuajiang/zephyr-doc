:orphan:

.. title:: I2C_INIT_PRIORITY

.. option:: CONFIG_I2C_INIT_PRIORITY:
.. _CONFIG_I2C_INIT_PRIORITY:

I2C device driver initialization priority.



:Symbol:           I2C_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if I2C (value: "n")
:Default values:

 *  60 (value: "n")
 *   Condition: I2C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:75