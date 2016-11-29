:orphan:

.. title:: SOC_ATMEL_SAM3_WAIT_MODE

.. option:: CONFIG_SOC_ATMEL_SAM3_WAIT_MODE:
.. _CONFIG_SOC_ATMEL_SAM3_WAIT_MODE:

For JTAG debugging CPU clock (HCLK) should not stop. In order
to achieve this, make CPU go to Wait mode instead of Sleep
mode while using external crystal oscillator for main clock.



:Symbol:           SOC_ATMEL_SAM3_WAIT_MODE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Atmel SAM3 goes to Wait mode instead of Sleep mode" if SOC_ATMEL_SAM3_EXT_MAINCK (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: DEBUG && SOC_ATMEL_SAM3_EXT_MAINCK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARM && SOC_ATMEL_SAM3 && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/atmel_sam3/Kconfig:83