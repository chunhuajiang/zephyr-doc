:orphan:

.. title:: PWM_PCA9685_0

.. option:: CONFIG_PWM_PCA9685_0:
.. _CONFIG_PWM_PCA9685_0:

Enable config options for the PCA9685 I2C-based PWM chip #0.



:Symbol:           PWM_PCA9685_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PCA9685 PWM chip #0" if PWM_PCA9685 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_PCA9685 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM && I2C && BOARD_GALILEO && PWM_PCA9685 (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:40
 * ../boards/x86/galileo/Kconfig.defconfig:109