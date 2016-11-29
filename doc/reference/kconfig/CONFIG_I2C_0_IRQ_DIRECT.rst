:orphan:

.. title:: I2C_0_IRQ_DIRECT

.. option:: CONFIG_I2C_0_IRQ_DIRECT:
.. _CONFIG_I2C_0_IRQ_DIRECT:

When interrupts fire, the driver's ISR function is being called directly.



:Symbol:           I2C_0_IRQ_DIRECT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Direct Hardware Interrupt"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:118