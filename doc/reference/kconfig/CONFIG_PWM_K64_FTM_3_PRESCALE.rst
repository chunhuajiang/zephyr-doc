:orphan:

.. title:: PWM_K64_FTM_3_PRESCALE

.. option:: CONFIG_PWM_K64_FTM_3_PRESCALE:
.. _CONFIG_PWM_K64_FTM_3_PRESCALE:

Specify the FTM timer prescale value.  The valid values are
1, 2, 4, 8, 16, 32, 64, or 128



:Symbol:           PWM_K64_FTM_3_PRESCALE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM3 prescale value" if PWM_K64_FTM_3 (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: PWM_K64_FTM_3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:397