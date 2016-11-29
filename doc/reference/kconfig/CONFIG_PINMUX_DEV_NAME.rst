:orphan:

.. title:: PINMUX_DEV_NAME

.. option:: CONFIG_PINMUX_DEV_NAME:
.. _CONFIG_PINMUX_DEV_NAME:

The name of the pinmux dev driver.



:Symbol:           PINMUX_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Configure pinmux for early board testing" if PINMUX_DEV (value: "n")
:Default values:

 *  "PINMUX_DEV"
 *   Condition: PINMUX_DEV (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/dev/Kconfig:28