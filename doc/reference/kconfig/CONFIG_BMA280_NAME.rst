:orphan:

.. title:: BMA280_NAME

.. option:: CONFIG_BMA280_NAME:
.. _CONFIG_BMA280_NAME:

Device name with which the sensor is identified.



:Symbol:           BMA280_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver name" if BMA280 (value: "n")
:Default values:

 *  "BMA280"
 *   Condition: BMA280_CHIP_BMA280 && BMA280 (value: "n")
 *  "BMC150_ACCEL"
 *   Condition: BMA280_CHIP_BMC150_ACCEL && BMA280 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bma280/Kconfig:49