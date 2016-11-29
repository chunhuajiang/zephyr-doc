:orphan:

.. title:: CLOCK_CONTROL_STM32F4X_DEVICE_INIT_PRIORITY

.. option:: CONFIG_CLOCK_CONTROL_STM32F4X_DEVICE_INIT_PRIORITY:
.. _CONFIG_CLOCK_CONTROL_STM32F4X_DEVICE_INIT_PRIORITY:

This option controls the priority of clock control
device initialization. Higher priority ensures that the device
is initialized earlier in the startup cycle. If unsure, leave
at default value 1



:Symbol:           CLOCK_CONTROL_STM32F4X_DEVICE_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Clock Control Device Priority" if CLOCK_CONTROL_STM32F4X (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: CLOCK_CONTROL_STM32F4X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_STM32F4X && CLOCK_CONTROL (value: "n")
:Locations:
 * ../drivers/clock_control/Kconfig.stm32f4x:30