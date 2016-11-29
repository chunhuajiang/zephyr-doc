:orphan:

.. title:: PWM_K64_FTM_1_PERIOD

.. option:: CONFIG_PWM_K64_FTM_1_PERIOD:
.. _CONFIG_PWM_K64_FTM_1_PERIOD:

Specify the FTM1 PWM period in ticks



:Symbol:           PWM_K64_FTM_1_PERIOD
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM1 period value" if PWM_K64_FTM_1 (value: "n")
:Default values:

 *  65535 (value: "n")
 *   Condition: PWM_K64_FTM_1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:187