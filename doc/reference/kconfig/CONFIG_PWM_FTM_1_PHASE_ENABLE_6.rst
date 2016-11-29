:orphan:

.. title:: PWM_FTM_1_PHASE_ENABLE_6

.. option:: CONFIG_PWM_FTM_1_PHASE_ENABLE_6:
.. _CONFIG_PWM_FTM_1_PHASE_ENABLE_6:

Allow a phase offset on FTM1 channel 6.  This configures
channels 6 and 7 to be in combine mode therefore
channel 7 is not valid as an output signal.
Note: phase is an unsupported feature.



:Symbol:           PWM_FTM_1_PHASE_ENABLE_6
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FTM1 Enable Phase for channel 6" if PWM_K64_FTM_1 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_K64_FTM_1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:262