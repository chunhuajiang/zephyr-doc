:orphan:

.. title:: IWDG_STM32

.. option:: CONFIG_IWDG_STM32:
.. _CONFIG_IWDG_STM32:

Enable IWDG driver for STM32 line of MCUs



:Symbol:           IWDG_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Independent Watchdog (IWDG) Driver for STM32 family of MCUs"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 WATCHDOG && SOC_SERIES_STM32F1X (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig.stm32:20
 * ../arch/arm/soc/st_stm32/stm32f1/Kconfig.defconfig.series:31