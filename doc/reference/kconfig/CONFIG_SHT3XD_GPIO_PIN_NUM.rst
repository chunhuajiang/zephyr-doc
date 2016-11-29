:orphan:

.. title:: SHT3XD_GPIO_PIN_NUM

.. option:: CONFIG_SHT3XD_GPIO_PIN_NUM:
.. _CONFIG_SHT3XD_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the
SHT3xD chip will be received.



:Symbol:           SHT3XD_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if SHT3XD && SHT3XD_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: SHT3XD && SHT3XD_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:92