:orphan:

.. title:: TMP007_GPIO_PIN_NUM

.. option:: CONFIG_TMP007_GPIO_PIN_NUM:
.. _CONFIG_TMP007_GPIO_PIN_NUM:

The number of the GPIO pin on which the interrupt signal from the
TMP007 chip will be received.



:Symbol:           TMP007_GPIO_PIN_NUM
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Interrupt GPIO pin number" if TMP007 && TMP007_TRIGGER (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: TMP007 && TMP007_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:99