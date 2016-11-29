:orphan:

.. title:: SOC_ATMEL_SAM3_PLLA_MULA

.. option:: CONFIG_SOC_ATMEL_SAM3_PLLA_MULA:
.. _CONFIG_SOC_ATMEL_SAM3_PLLA_MULA:

This is the multiplier (MULA) used by the PLL.
The processor clock is (MAINCK * (MULA + 1) / DIVA).

Board config file can override this settings
for a particular board.

With default of MULA == 6, and DIVA == 1,
PLL is running at 7 times of main clock.



:Symbol:           SOC_ATMEL_SAM3_PLLA_MULA
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  0x06 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARM && SOC_ATMEL_SAM3 && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/atmel_sam3/Kconfig:57