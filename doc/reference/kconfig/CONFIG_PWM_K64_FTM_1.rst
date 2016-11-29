:orphan:

.. title:: PWM_K64_FTM_1

.. option:: CONFIG_PWM_K64_FTM_1:
.. _CONFIG_PWM_K64_FTM_1:

Enable config PWM options for FTM1 source module.



:Symbol:           PWM_K64_FTM_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K64 FTM PWM Module 1" if PWM_K64_FTM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_K64_FTM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:165