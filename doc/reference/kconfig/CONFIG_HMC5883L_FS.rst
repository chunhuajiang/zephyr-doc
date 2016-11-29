:orphan:

.. title:: HMC5883L_FS

.. option:: CONFIG_HMC5883L_FS:
.. _CONFIG_HMC5883L_FS:

Magnetometer full-scale range.
An X value for the config represents a range of +/- X gauss. Valid
values are 0.88, 1.3, 1.9, 2.5, 4, 4.7, 5.6 and 8.1.


:Symbol:           HMC5883L_FS
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Full-scale range" if HMC5883L (value: "n")
:Default values:

 *  "1.3"
 *   Condition: HMC5883L (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:115