:orphan:

.. title:: PWM_PCA9685_0_I2C_MASTER_DEV_NAME

.. option:: CONFIG_PWM_PCA9685_0_I2C_MASTER_DEV_NAME:
.. _CONFIG_PWM_PCA9685_0_I2C_MASTER_DEV_NAME:

Specify the device name of the I2C master device to which this
PCA9685 chip #0 is binded.



:Symbol:           PWM_PCA9685_0_I2C_MASTER_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C Master where PCA9685 PWM chip #0 is connected" if PWM_PCA9685_0 (value: "n")
:Default values:

 *  ""
 *   Condition: PWM_PCA9685_0 (value: "n")
 *  I2C_0_NAME (value: "")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && I2C && BOARD_GALILEO && PWM_PCA9685 && PWM_PCA9685_0 (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:61
 * ../boards/x86/galileo/Kconfig.defconfig:118