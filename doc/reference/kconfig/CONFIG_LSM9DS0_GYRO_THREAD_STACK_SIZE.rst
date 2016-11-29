:orphan:

.. title:: LSM9DS0_GYRO_THREAD_STACK_SIZE

.. option:: CONFIG_LSM9DS0_GYRO_THREAD_STACK_SIZE:
.. _CONFIG_LSM9DS0_GYRO_THREAD_STACK_SIZE:

Specify the internal thread stack size.



:Symbol:           LSM9DS0_GYRO_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if LSM9DS0_GYRO_TRIGGERS (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: LSM9DS0_GYRO_TRIGGERS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_gyro/Kconfig:120