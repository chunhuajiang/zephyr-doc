:orphan:

.. title:: PWM_PCA9685_0_I2C_ADDR

.. option:: CONFIG_PWM_PCA9685_0_I2C_ADDR:
.. _CONFIG_PWM_PCA9685_0_I2C_ADDR:

Specify the I2C slave address for the PCA9685 I2C-based PWM chip #0.



:Symbol:           PWM_PCA9685_0_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCA9685 PWM chip #0 I2C slave address" if PWM_PCA9685_0 (value: "n")
:Default values:

 *  0x0 (value: "n")
 *   Condition: PWM_PCA9685_0 (value: "n")
 *  0x47 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && I2C && BOARD_GALILEO && PWM_PCA9685 && PWM_PCA9685_0 (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:54
 * ../boards/x86/galileo/Kconfig.defconfig:116