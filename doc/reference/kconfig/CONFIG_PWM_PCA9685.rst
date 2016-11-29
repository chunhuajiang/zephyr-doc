:orphan:

.. title:: PWM_PCA9685

.. option:: CONFIG_PWM_PCA9685:
.. _CONFIG_PWM_PCA9685:

Enable driver for PCA9685 I2C-based PWM chip.



:Symbol:           PWM_PCA9685
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCA9685 I2C-based PWM chip" if PWM && I2C (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM && I2C (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && I2C && BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:23
 * ../boards/x86/galileo/Kconfig.defconfig:104