:orphan:

.. title:: PINMUX_DEV_ATMEL_SAM3X

.. option:: CONFIG_PINMUX_DEV_ATMEL_SAM3X:
.. _CONFIG_PINMUX_DEV_ATMEL_SAM3X:

Enables the pinmux dev driver for boards based on the
Atmel SAM3X family of microcontrollers.
default n



:Symbol:           PINMUX_DEV_ATMEL_SAM3X
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable pinmux dev driver for Atmel SAM3X boards" if PINMUX_DEV && SOC_ATMEL_SAM3X8E (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:35