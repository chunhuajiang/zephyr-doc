:orphan:

.. title:: PWM_K64_FTM_2_PERIOD

.. option:: CONFIG_PWM_K64_FTM_2_PERIOD:
.. _CONFIG_PWM_K64_FTM_2_PERIOD:

Specify the FTM2 PWM period in ticks



:Symbol:           PWM_K64_FTM_2_PERIOD
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM2 period value" if PWM_K64_FTM_2 (value: "n")
:Default values:

 *  65535 (value: "n")
 *   Condition: PWM_K64_FTM_2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:296