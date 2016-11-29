:orphan:

.. title:: PINMUX_DEV_STM32

.. option:: CONFIG_PINMUX_DEV_STM32:
.. _CONFIG_PINMUX_DEV_STM32:

Enables the STM32 pinmux dev driver.
default n



:Symbol:           PINMUX_DEV_STM32
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable pinmux dev driver for the ST STM32 family." if PINMUX_DEV && SOC_FAMILY_STM32 (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:64