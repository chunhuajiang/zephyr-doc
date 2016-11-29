:orphan:

.. title:: PINMUX_DEV_QMSI

.. option:: CONFIG_PINMUX_DEV_QMSI:
.. _CONFIG_PINMUX_DEV_QMSI:

Enables the pinmux dev driver for QMSI supported boards.
default n



:Symbol:           PINMUX_DEV_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable QMSI pinmux dev driver" if PINMUX_DEV && QMSI (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:57