:orphan:

.. title:: IWDG_STM32_RELOAD_COUNTER

.. option:: CONFIG_IWDG_STM32_RELOAD_COUNTER:
.. _CONFIG_IWDG_STM32_RELOAD_COUNTER:

Configure the value to be loaded into the watchdog's counter each
time a reload operation is performed. This value combined with
prescaler setting defines the watchdog countdown time.



:Symbol:           IWDG_STM32_RELOAD_COUNTER
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0, 4095]
:Prompts:

 *  "Value for IWDG counter" if IWDG_STM32 (value: "n")
:Default values:

 *  2048 (value: "n")
 *   Condition: IWDG_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 && WATCHDOG (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig.stm32:37