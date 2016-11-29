:orphan:

.. title:: LIS3MDL_FS

.. option:: CONFIG_LIS3MDL_FS:
.. _CONFIG_LIS3MDL_FS:

Magnetometer full-scale range.
An X value for the config represents a range of +/- X gauss. Valid
values are 4, 8, 12 and 16.


:Symbol:           LIS3MDL_FS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Full-scale range" if LIS3MDL (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: LIS3MDL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:125