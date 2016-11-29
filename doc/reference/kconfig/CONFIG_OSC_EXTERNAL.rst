:orphan:

.. title:: OSC_EXTERNAL

.. option:: CONFIG_OSC_EXTERNAL:
.. _CONFIG_OSC_EXTERNAL:

Set this option to use the oscillator in external reference clock mode.



:Symbol:           OSC_EXTERNAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "External reference clock"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_OSC && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:63