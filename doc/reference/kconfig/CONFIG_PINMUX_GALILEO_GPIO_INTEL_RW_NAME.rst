:orphan:

.. title:: PINMUX_GALILEO_GPIO_INTEL_RW_NAME

.. option:: CONFIG_PINMUX_GALILEO_GPIO_INTEL_RW_NAME:
.. _CONFIG_PINMUX_GALILEO_GPIO_INTEL_RW_NAME:

The name of the Legacy Bridge Resume Well GPIO with
GPIO_SUS<0>..GPIO_SUS<5> in the schematic.


:Symbol:           PINMUX_GALILEO_GPIO_INTEL_RW_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Name of the Legacy Bridge Resume Well GPIO" if PINMUX && BOARD_GALILEO (value: "n")
:Default values:

 *  "GPIO_M1"
 *   Condition: PINMUX && BOARD_GALILEO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PINMUX && BOARD_GALILEO (value: "n")
:Locations:
 * ../boards/x86/galileo/Kconfig:65