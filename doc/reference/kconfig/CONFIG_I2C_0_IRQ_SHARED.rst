:orphan:

.. title:: I2C_0_IRQ_SHARED

.. option:: CONFIG_I2C_0_IRQ_SHARED:
.. _CONFIG_I2C_0_IRQ_SHARED:

When interrupts fire, the shared IRQ driver is notified. Then the shared IRQ
driver dispatches the interrupt to other drivers.



:Symbol:           I2C_0_IRQ_SHARED
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared IRQ" if SHARED_IRQ (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_I2C_SHARED_IRQ` if SHARED_IRQ (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 I2C (value: "n")
:Locations:
 * ../drivers/i2c/Kconfig:123