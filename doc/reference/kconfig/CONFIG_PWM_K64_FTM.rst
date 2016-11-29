:orphan:

.. title:: PWM_K64_FTM

.. option:: CONFIG_PWM_K64_FTM:
.. _CONFIG_PWM_K64_FTM:

Enable Pulse Width Modulation driver for Freescale
K64 Flex Timer Module (FTM).



:Symbol:           PWM_K64_FTM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PWM with Freescale K64 Flex Timer Module (FTM)" if PWM && SOC_MK64F12 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM && SOC_MK64F12 (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.k64:24
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:51