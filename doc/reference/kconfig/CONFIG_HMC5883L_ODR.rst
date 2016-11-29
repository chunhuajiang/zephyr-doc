:orphan:

.. title:: HMC5883L_ODR

.. option:: CONFIG_HMC5883L_ODR:
.. _CONFIG_HMC5883L_ODR:

Magnetometer output data rate expressed in samples per second.
Data rates supported by the chip are 0.75, 1.5, 3, 7.5, 15, 30
and 75.



:Symbol:           HMC5883L_ODR
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Output data rate" if HMC5883L (value: "n")
:Default values:

 *  "15"
 *   Condition: HMC5883L (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:105