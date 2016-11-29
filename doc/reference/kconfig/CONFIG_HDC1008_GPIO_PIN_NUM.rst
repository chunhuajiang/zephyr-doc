:orphan:

.. title:: HDC1008_GPIO_PIN_NUM

.. option:: CONFIG_HDC1008_GPIO_PIN_NUM:
.. _CONFIG_HDC1008_GPIO_PIN_NUM:

The number of the GPIO on which the data-ready signal from the HDC1008
chip will be received.


:Symbol:           HDC1008_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if HDC1008 (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: HDC1008 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hdc1008/Kconfig:64