:orphan:

.. title:: LSM6DS0_ACCEL_SAMPLING_RATE

.. option:: CONFIG_LSM6DS0_ACCEL_SAMPLING_RATE:
.. _CONFIG_LSM6DS0_ACCEL_SAMPLING_RATE:

Specify the default accelerometer output data rate expressed in
samples per second (Hz).
Data rates supported by the chip are 0, 10, 50, 119, 238, 476, 952.



:Symbol:           LSM6DS0_ACCEL_SAMPLING_RATE
:Type:             int
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

 *  10 (value: "n")
 *   Condition: LIS3MDL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LSM6DS0 (value: "n")
:Locations:
 * ../drivers/sensor/lsm6ds0/Kconfig:160