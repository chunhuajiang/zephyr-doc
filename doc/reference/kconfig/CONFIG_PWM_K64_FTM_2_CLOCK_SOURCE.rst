:orphan:

.. title:: PWM_K64_FTM_2_CLOCK_SOURCE

.. option:: CONFIG_PWM_K64_FTM_2_CLOCK_SOURCE:
.. _CONFIG_PWM_K64_FTM_2_CLOCK_SOURCE:

Specify K64 FTM2 clock source



:Symbol:           PWM_K64_FTM_2_CLOCK_SOURCE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  0 (value: "n")
 *   Condition: PWM_K64_FTM_2_CLOCK_SOURCE_NONE && PWM_K64_FTM_2 (value: "n")
 *  1 (value: "n")
 *   Condition: PWM_K64_FTM_2_CLOCK_SOURCE_SYSTEM && PWM_K64_FTM_2 (value: "n")
 *  2 (value: "n")
 *   Condition: PWM_K64_FTM_2_CLOCK_SOURCE_FIXED && PWM_K64_FTM_2 (value: "n")
 *  3 (value: "n")
 *   Condition: PWM_K64_FTM_2_CLOCK_SOURCE_EXTERNAL && PWM_K64_FTM_2 (value: "n")
 *  4 (value: "n")
 *   Condition: PWM_K64_FTM_2_CLOCK_SOURCE_QUAD && PWM_K64_FTM_2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:329