:orphan:

.. title:: PWM_PCA9685_INIT_PRIORITY

.. option:: CONFIG_PWM_PCA9685_INIT_PRIORITY:
.. _CONFIG_PWM_PCA9685_INIT_PRIORITY:

Device driver initialization priority.



:Symbol:           PWM_PCA9685_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if PWM_PCA9685 (value: "n")
:Default values:

 *  70 (value: "n")
 *   Condition: PWM_PCA9685 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_PCA9685 && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.pca9685:32