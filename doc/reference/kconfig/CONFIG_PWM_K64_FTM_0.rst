:orphan:

.. title:: PWM_K64_FTM_0

.. option:: CONFIG_PWM_K64_FTM_0:
.. _CONFIG_PWM_K64_FTM_0:

Enable config PWM options for FTM0 source module.



:Symbol:           PWM_K64_FTM_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "K64 FTM PWM Module 0" if PWM_K64_FTM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_K64_FTM (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_K64_FTM && BOARD_FRDM_K64F (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:56
 * ../boards/arm/hexiwear_k64/Kconfig.defconfig:147
 * ../boards/arm/frdm_k64f/Kconfig.defconfig:147