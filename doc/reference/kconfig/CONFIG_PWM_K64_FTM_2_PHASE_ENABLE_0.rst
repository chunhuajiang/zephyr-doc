:orphan:

.. title:: PWM_K64_FTM_2_PHASE_ENABLE_0

.. option:: CONFIG_PWM_K64_FTM_2_PHASE_ENABLE_0:
.. _CONFIG_PWM_K64_FTM_2_PHASE_ENABLE_0:

Allow a phase offset on FTM2 channel 0.  This configures
channels 0 and 1 to be in combine mode therefore
channel 1 is not valid as an output signal.
Note: phase is an unsupported feature.



:Symbol:           PWM_K64_FTM_2_PHASE_ENABLE_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM2 Enable Phase for channel 0" if PWM_K64_FTM_2 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_K64_FTM_2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:341