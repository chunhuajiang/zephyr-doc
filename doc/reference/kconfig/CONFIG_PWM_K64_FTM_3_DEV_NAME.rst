:orphan:

.. title:: PWM_K64_FTM_3_DEV_NAME

.. option:: CONFIG_PWM_K64_FTM_3_DEV_NAME:
.. _CONFIG_PWM_K64_FTM_3_DEV_NAME:

Specify the device name for the FTM3 source module.



:Symbol:           PWM_K64_FTM_3_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K64 FTM PWM Module 3 Device Name" if PWM_K64_FTM_3 (value: "n")
:Default values:

 *  "PWM_3"
 *   Condition: PWM_K64_FTM_3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:390