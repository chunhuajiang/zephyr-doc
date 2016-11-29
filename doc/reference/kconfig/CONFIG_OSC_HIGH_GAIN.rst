:orphan:

.. title:: OSC_HIGH_GAIN

.. option:: CONFIG_OSC_HIGH_GAIN:
.. _CONFIG_OSC_HIGH_GAIN:

Set this option to use the oscillator in high-gain mode.



:Symbol:           OSC_HIGH_GAIN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "High gain oscillator"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_OSC && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:73