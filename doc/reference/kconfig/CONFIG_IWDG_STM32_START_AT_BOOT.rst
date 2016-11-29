:orphan:

.. title:: IWDG_STM32_START_AT_BOOT

.. option:: CONFIG_IWDG_STM32_START_AT_BOOT:
.. _CONFIG_IWDG_STM32_START_AT_BOOT:

Enable this setting to allow IWDG to be automatically started
during device initialization. Note that once IWDG is started
it must be reloaded before the counter reaches 0, otherwise
the MCU will be reset.



:Symbol:           IWDG_STM32_START_AT_BOOT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Start IWDG during boot" if IWDG_STM32 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: IWDG_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 && WATCHDOG (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig.stm32:47