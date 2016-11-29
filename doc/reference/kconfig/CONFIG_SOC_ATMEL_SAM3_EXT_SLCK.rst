:orphan:

.. title:: SOC_ATMEL_SAM3_EXT_SLCK

.. option:: CONFIG_SOC_ATMEL_SAM3_EXT_SLCK:
.. _CONFIG_SOC_ATMEL_SAM3_EXT_SLCK:

Says y if you want to use external 32 kHz crystal
oscillator to drive the slow clock. Note that this
adds a few seconds to boot time, as the crystal
needs to stabilize after power-up.

Says n if you do not need accraute and precise timers.
The slow clock will be driven by the internal fast
RC oscillator running at 32 kHz.



:Symbol:           SOC_ATMEL_SAM3_EXT_SLCK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 to use external crystal oscillator for slow clock"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARM && SOC_ATMEL_SAM3 && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/atmel_sam3/Kconfig:27