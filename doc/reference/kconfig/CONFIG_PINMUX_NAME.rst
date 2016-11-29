:orphan:

.. title:: PINMUX_NAME

.. option:: CONFIG_PINMUX_NAME:
.. _CONFIG_PINMUX_NAME:

The name of the pinmux driver.



:Symbol:           PINMUX_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Pinmux driver name" if PINMUX (value: "n")
:Default values:

 *  "PINMUX"
 *   Condition: PINMUX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig:30