:orphan:

.. title:: IWDG_STM32_DEVICE_NAME

.. option:: CONFIG_IWDG_STM32_DEVICE_NAME:
.. _CONFIG_IWDG_STM32_DEVICE_NAME:

Set the name used by IWDG device during registration.



:Symbol:           IWDG_STM32_DEVICE_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Independent Watchdog (IWDG)" if IWDG_STM32 (value: "n")
:Default values:

 *  "IWDG"
 *   Condition: IWDG_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FAMILY_STM32 && WATCHDOG (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig.stm32:57