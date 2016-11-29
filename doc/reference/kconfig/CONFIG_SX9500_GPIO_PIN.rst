:orphan:

.. title:: SX9500_GPIO_PIN

.. option:: CONFIG_SX9500_GPIO_PIN:
.. _CONFIG_SX9500_GPIO_PIN:

The configuration item CONFIG_SX9500_GPIO_PIN:

:Symbol:           SX9500_GPIO_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO pin for SX9500 interrupt" if SX9500 && SX9500_TRIGGER (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: SX9500 && SX9500_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sx9500/Kconfig:87