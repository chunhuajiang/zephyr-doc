:orphan:

.. title:: PINMUX_STM32_DEVICE_INITIALIZATION_PRIORITY

.. option:: CONFIG_PINMUX_STM32_DEVICE_INITIALIZATION_PRIORITY:
.. _CONFIG_PINMUX_STM32_DEVICE_INITIALIZATION_PRIORITY:

This option controls the priority of pinmux device initialization.
Higher priority ensures that the device is initialized earlier in
the startup cycle. Note that the pinmux device needs to be initialized
after clock control device, but possibly before all other devices.
If unsure, leave at default value 2


:Symbol:           PINMUX_STM32_DEVICE_INITIALIZATION_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device initialization priority STM32 pinmux" if PINMUX_STM32 (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: PINMUX_STM32 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig.stm32:24