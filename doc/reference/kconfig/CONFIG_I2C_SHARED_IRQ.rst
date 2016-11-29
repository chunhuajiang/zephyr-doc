:orphan:

.. title:: I2C_SHARED_IRQ

.. option:: CONFIG_I2C_SHARED_IRQ:
.. _CONFIG_I2C_SHARED_IRQ:

The configuration item CONFIG_I2C_SHARED_IRQ:

:Symbol:           I2C_SHARED_IRQ
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: I2C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SHARED_IRQ && I2C && I2C_0_IRQ_SHARED (value: "n")
:Additional dependencies from enclosing menus and ifs:
 I2C (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:108