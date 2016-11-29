:orphan:

.. title:: PWM_K64_FTM_3_PHASE_ENABLE_2

.. option:: CONFIG_PWM_K64_FTM_3_PHASE_ENABLE_2:
.. _CONFIG_PWM_K64_FTM_3_PHASE_ENABLE_2:

Allow a phase offset on FTM3 channel 2.  This configures
channels 2 and 3 to be in combine mode therefore
channel 3 is not valid as an output signal.
Note: phase is an unsupported feature.



:Symbol:           PWM_K64_FTM_3_PHASE_ENABLE_2
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM3 Enable Phase for channel 2" if PWM_K64_FTM_3 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_K64_FTM_3 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:460