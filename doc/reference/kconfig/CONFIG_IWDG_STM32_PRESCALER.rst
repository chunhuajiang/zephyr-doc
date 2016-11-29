:orphan:

.. title:: IWDG_STM32_PRESCALER

.. option:: CONFIG_IWDG_STM32_PRESCALER:
.. _CONFIG_IWDG_STM32_PRESCALER:

Set the prescaler divider for the clock feeding the Independent
Watchdog. Higher values indicate that the watchdog will need to
be reloaded more frequently. Allowed values: 4, 8, 16, 32, 64,
128, 256. This setting combined with reload counter defines the
watchdog countdown time.



:Symbol:           IWDG_STM32_PRESCALER
:Type:             int
:Value:            "4"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [4, 256]
:Prompts:

 *  "Prescaler divider for clock feeding the IWDG" if IWDG_STM32 (value: "n")
:Default values:

 *  4 (value: "n")
 *   Condition: IWDG_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 && WATCHDOG (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig.stm32:25