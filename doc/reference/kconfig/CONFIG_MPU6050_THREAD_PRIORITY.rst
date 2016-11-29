:orphan:

.. title:: MPU6050_THREAD_PRIORITY

.. option:: CONFIG_MPU6050_THREAD_PRIORITY:
.. _CONFIG_MPU6050_THREAD_PRIORITY:

Priority of thread used by the driver to handle interrupts.



:Symbol:           MPU6050_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread priority" if MPU6050 && MPU6050_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: MPU6050 && MPU6050_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:102