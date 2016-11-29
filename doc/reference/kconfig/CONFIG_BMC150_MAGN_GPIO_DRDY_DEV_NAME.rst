:orphan:

.. title:: BMC150_MAGN_GPIO_DRDY_DEV_NAME

.. option:: CONFIG_BMC150_MAGN_GPIO_DRDY_DEV_NAME:
.. _CONFIG_BMC150_MAGN_GPIO_DRDY_DEV_NAME:

Specify the device name of the GPIO controller the BMC150_MAGN interrupt
is connected to.



:Symbol:           BMC150_MAGN_GPIO_DRDY_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device where BMC150_MAGN data ready interrupt is connected" if BMC150_MAGN_TRIGGER_DRDY (value: "n")
:Default values:

 *  GPIO_0 (value: "GPIO_0")
 *   Condition: BMC150_MAGN_TRIGGER_DRDY (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:122