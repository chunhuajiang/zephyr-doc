:orphan:

.. title:: PINMUX_GALILEO_PWM0_NAME

.. option:: CONFIG_PINMUX_GALILEO_PWM0_NAME:
.. _CONFIG_PINMUX_GALILEO_PWM0_NAME:

The name of the PWM LED expander labelled as PWM0 in the schematic.



:Symbol:           PINMUX_GALILEO_PWM0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Name of the PWM LED expander 0" if PINMUX && BOARD_GALILEO (value: "n")
:Default values:

 *  "PWM0"
 *   Condition: PINMUX && BOARD_GALILEO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX && BOARD_GALILEO (value: "n")
:Locations:
 * ../boards/x86/galileo/Kconfig:43