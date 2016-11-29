:orphan:

.. title:: BMC150_MAGN_GPIO_DRDY_INT_PIN

.. option:: CONFIG_BMC150_MAGN_GPIO_DRDY_INT_PIN:
.. _CONFIG_BMC150_MAGN_GPIO_DRDY_INT_PIN:

GPIO pin number for the data ready interrupt pin.


:Symbol:           BMC150_MAGN_GPIO_DRDY_INT_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO pin number for the data ready interrupt pin" if BMC150_MAGN_TRIGGER_DRDY (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: BMC150_MAGN_TRIGGER_DRDY (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:130