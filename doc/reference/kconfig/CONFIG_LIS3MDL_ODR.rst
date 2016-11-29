:orphan:

.. title:: LIS3MDL_ODR

.. option:: CONFIG_LIS3MDL_ODR:
.. _CONFIG_LIS3MDL_ODR:

Magnetometer output data rate expressed in samples per second.
Data rates supported by the chip are 0.625, 1.25, 2.5, 5, 10, 20,
40, 80, 155, 300, 560 and 1000.



:Symbol:           LIS3MDL_ODR
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Output data rate" if LIS3MDL (value: "n")
:Default values:

 *  "0.625"
 *   Condition: LIS3MDL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:115