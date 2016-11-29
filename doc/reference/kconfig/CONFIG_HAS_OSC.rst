:orphan:

.. title:: HAS_OSC

.. option:: CONFIG_HAS_OSC:
.. _CONFIG_HAS_OSC:

Set if the oscillator (OSC) module is present in the SoC.



:Symbol:           HAS_OSC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SOC_MK64F12 && ARM (value: "n")
:Additional dependencies from enclosing menus and ifs:
 ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:39