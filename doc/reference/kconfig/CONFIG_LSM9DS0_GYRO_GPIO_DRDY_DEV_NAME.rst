:orphan:

.. title:: LSM9DS0_GYRO_GPIO_DRDY_DEV_NAME

.. option:: CONFIG_LSM9DS0_GYRO_GPIO_DRDY_DEV_NAME:
.. _CONFIG_LSM9DS0_GYRO_GPIO_DRDY_DEV_NAME:

Specify the device name of the GPIO controller the BMC150_MAGN interrupt
is connected to.



:Symbol:           LSM9DS0_GYRO_GPIO_DRDY_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device where LSM9DS0_GYRO data ready interrupt is connected" if LSM9DS0_GYRO_TRIGGER_DRDY (value: "n")
:Default values:

 *  GPIO_0 (value: "GPIO_0")
 *   Condition: LSM9DS0_GYRO_TRIGGER_DRDY (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lsm9ds0_gyro/Kconfig:132