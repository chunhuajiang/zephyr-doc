:orphan:

.. title:: HMC5883L_GPIO_PIN_NUM

.. option:: CONFIG_HMC5883L_GPIO_PIN_NUM:
.. _CONFIG_HMC5883L_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the
HMC5883L chip will be received.



:Symbol:           HMC5883L_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if HMC5883L && HMC5883L_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: HMC5883L && HMC5883L_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:80