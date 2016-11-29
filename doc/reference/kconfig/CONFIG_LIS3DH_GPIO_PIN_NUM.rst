:orphan:

.. title:: LIS3DH_GPIO_PIN_NUM

.. option:: CONFIG_LIS3DH_GPIO_PIN_NUM:
.. _CONFIG_LIS3DH_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the LIS3DH
chip will be received.



:Symbol:           LIS3DH_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if LIS3DH && LIS3DH_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: LIS3DH && LIS3DH_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3dh/Kconfig:93