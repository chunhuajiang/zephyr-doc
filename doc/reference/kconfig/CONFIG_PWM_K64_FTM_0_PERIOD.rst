:orphan:

.. title:: PWM_K64_FTM_0_PERIOD

.. option:: CONFIG_PWM_K64_FTM_0_PERIOD:
.. _CONFIG_PWM_K64_FTM_0_PERIOD:

Specify the FTM0 PWM period in ticks



:Symbol:           PWM_K64_FTM_0_PERIOD
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K64 FTM0 period value" if PWM_K64_FTM_0 (value: "n")
:Default values:

 *  65535 (value: "n")
 *   Condition: PWM_K64_FTM_0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:78