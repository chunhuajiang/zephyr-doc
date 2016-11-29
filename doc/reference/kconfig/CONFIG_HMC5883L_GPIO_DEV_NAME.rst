:orphan:

.. title:: HMC5883L_GPIO_DEV_NAME

.. option:: CONFIG_HMC5883L_GPIO_DEV_NAME:
.. _CONFIG_HMC5883L_GPIO_DEV_NAME:

The device name of the GPIO device to which the HMC5883L interrupt
pin is connected.



:Symbol:           HMC5883L_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if HMC5883L && HMC5883L_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: HMC5883L && HMC5883L_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:71