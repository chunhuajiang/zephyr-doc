:orphan:

.. title:: HTS221_GPIO_PIN_NUM

.. option:: CONFIG_HTS221_GPIO_PIN_NUM:
.. _CONFIG_HTS221_GPIO_PIN_NUM:

The number of the GPIO on which the interrupt signal from the HTS221
chip will be received.



:Symbol:           HTS221_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if HTS221 && HTS221_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: HTS221 && HTS221_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:80