:orphan:

.. title:: PWM_K64_FTM_1_DEV_NAME

.. option:: CONFIG_PWM_K64_FTM_1_DEV_NAME:
.. _CONFIG_PWM_K64_FTM_1_DEV_NAME:

Specify the device name for the FTM1 source module.



:Symbol:           PWM_K64_FTM_1_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K64 FTM PWM Module 1 Device Name" if PWM_K64_FTM_1 (value: "n")
:Default values:

 *  "PWM_1"
 *   Condition: PWM_K64_FTM_1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:172