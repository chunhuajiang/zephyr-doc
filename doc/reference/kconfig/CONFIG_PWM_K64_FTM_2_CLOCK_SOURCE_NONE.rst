:orphan:

.. title:: PWM_K64_FTM_2_CLOCK_SOURCE_NONE

.. option:: CONFIG_PWM_K64_FTM_2_CLOCK_SOURCE_NONE:
.. _CONFIG_PWM_K64_FTM_2_CLOCK_SOURCE_NONE:

The configuration item CONFIG_PWM_K64_FTM_2_CLOCK_SOURCE_NONE:

:Symbol:           PWM_K64_FTM_2_CLOCK_SOURCE_NONE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "No clock selected (FTM counter disable)"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM && PWM_K64_FTM_2 (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:310