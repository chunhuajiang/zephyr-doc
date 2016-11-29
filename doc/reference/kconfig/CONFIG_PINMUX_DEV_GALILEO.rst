:orphan:

.. title:: PINMUX_DEV_GALILEO

.. option:: CONFIG_PINMUX_DEV_GALILEO:
.. _CONFIG_PINMUX_DEV_GALILEO:

Enables the pinmux dev driver for the Galileo board.
default n



:Symbol:           PINMUX_DEV_GALILEO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable pinmux dev driver for Galileo" if PINMUX_DEV && BOARD_GALILEO (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:50