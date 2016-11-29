:orphan:

.. title:: PWM_PCA9685_0_DEV_NAME

.. option:: CONFIG_PWM_PCA9685_0_DEV_NAME:
.. _CONFIG_PWM_PCA9685_0_DEV_NAME:

Specify the device name for the PCA9685 I2C-based PWM chip #0.



:Symbol:           PWM_PCA9685_0_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCA9685 PWM chip #0 Device Name" if PWM_PCA9685_0 (value: "n")
:Default values:

 *  "PWM_0"
 *   Condition: PWM_PCA9685_0 (value: "n")
 *  "PWM0"
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && I2C && BOARD_GALILEO && PWM_PCA9685 && PWM_PCA9685_0 (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:47
 * ../boards/x86/galileo/Kconfig.defconfig:114