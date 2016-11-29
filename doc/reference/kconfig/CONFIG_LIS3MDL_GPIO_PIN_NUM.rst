:orphan:

.. title:: LIS3MDL_GPIO_PIN_NUM

.. option:: CONFIG_LIS3MDL_GPIO_PIN_NUM:
.. _CONFIG_LIS3MDL_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the LIS3MDL
chip will be received.



:Symbol:           LIS3MDL_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if LIS3MDL && LIS3MDL_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: LIS3MDL && LIS3MDL_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:90