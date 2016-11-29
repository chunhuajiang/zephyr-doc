:orphan:

.. title:: PINMUX_DEV

.. option:: CONFIG_PINMUX_DEV:
.. _CONFIG_PINMUX_DEV:

Enables the use of the pinmux_set and pinmux_get functions for early
prototyping on new hardware.  WARNING: When using these options, it
is possible to permanently damage the hardware.



:Symbol:           PINMUX_DEV
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Configure pinmux for early board testing" if PINMUX (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PINMUX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:19