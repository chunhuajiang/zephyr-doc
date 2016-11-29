:orphan:

.. title:: ISL29035_GPIO_PIN_NUM

.. option:: CONFIG_ISL29035_GPIO_PIN_NUM:
.. _CONFIG_ISL29035_GPIO_PIN_NUM:

The number of the GPIO pin to which the ISL29035 interrupt pin is
connected.



:Symbol:           ISL29035_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO pin number" if ISL29035 && ISL29035_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: ISL29035 && ISL29035_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:165