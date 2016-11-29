:orphan:

.. title:: MPU6050_THREAD_STACK_SIZE

.. option:: CONFIG_MPU6050_THREAD_STACK_SIZE:
.. _CONFIG_MPU6050_THREAD_STACK_SIZE:

Stack size of thread used by the driver to handle interrupts.



:Symbol:           MPU6050_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if MPU6050 && MPU6050_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: MPU6050 && MPU6050_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mpu6050/Kconfig:110