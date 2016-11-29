:orphan:

.. title:: OSC_LOW_POWER

.. option:: CONFIG_OSC_LOW_POWER:
.. _CONFIG_OSC_LOW_POWER:

Set this option to use the oscillator in low-power mode.



:Symbol:           OSC_LOW_POWER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Low power oscillator"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_OSC && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:68