:orphan:

.. title:: SOC_ATMEL_SAM3_EXT_MAINCK

.. option:: CONFIG_SOC_ATMEL_SAM3_EXT_MAINCK:
.. _CONFIG_SOC_ATMEL_SAM3_EXT_MAINCK:

The main clock is being used to drive the PLL, and
thus driving the processor clock.

Says y if you want to use external crystal oscillator
to drive the main clock. Note that this adds about
a second to boot time, as the crystal needs to
stabilize after power-up.

The crystal used here can be from 3 to 20 MHz.

Says n here will use the internal fast RC oscillator
running at 12 MHz.



:Symbol:           SOC_ATMEL_SAM3_EXT_MAINCK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 to use external crystal oscillator for main clock"
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
 * ../arch/arm/soc/atmel_sam3/Kconfig:40