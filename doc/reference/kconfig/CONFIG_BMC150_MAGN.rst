:orphan:

.. title:: BMC150_MAGN

.. option:: CONFIG_BMC150_MAGN:
.. _CONFIG_BMC150_MAGN:

Enable driver for BMC150 I2C-based magnetometer sensor.



:Symbol:           BMC150_MAGN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMC150_MAGN I2C Magnetometer Chip" if SENSOR && I2C && NANO_TIMEOUTS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SENSOR && I2C && NANO_TIMEOUTS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:19