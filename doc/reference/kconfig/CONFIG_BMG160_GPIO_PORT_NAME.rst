:orphan:

.. title:: BMG160_GPIO_PORT_NAME

.. option:: CONFIG_BMG160_GPIO_PORT_NAME:
.. _CONFIG_BMG160_GPIO_PORT_NAME:

The gpio controller the interrupt pin is atteched to.



:Symbol:           BMG160_GPIO_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO controller port name" if BMG160 && BMG160_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: BMG160 && BMG160_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:85