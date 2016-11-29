:orphan:

.. title:: SX9500_GPIO_CONTROLLER

.. option:: CONFIG_SX9500_GPIO_CONTROLLER:
.. _CONFIG_SX9500_GPIO_CONTROLLER:

Specify the device name of the GPIO controller the SX9500 interrupt
is connected to.



:Symbol:           SX9500_GPIO_CONTROLLER
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO controller for SX9500 interrupt" if SX9500 && SX9500_TRIGGER (value: "n")
:Default values:

 *  GPIO_0 (value: "GPIO_0")
 *   Condition: SX9500 && SX9500_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:79