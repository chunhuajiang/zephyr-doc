:orphan:

.. title:: SOC_PART_NUMBER_KINETIS_K6X

.. option:: CONFIG_SOC_PART_NUMBER_KINETIS_K6X:
.. _CONFIG_SOC_PART_NUMBER_KINETIS_K6X:

This string holds the full part number of the SoC. It is a hidden option
that you should not set directly. The part number selection choice defines
the default value for this string.



:Symbol:           SOC_PART_NUMBER_KINETIS_K6X
:Type:             string
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

 *  "MK64FN1M0CAJ12"
 *   Condition: SOC_PART_NUMBER_MK64FN1M0CAJ12 (value: "n")
 *  "MK64FN1M0VDC12"
 *   Condition: SOC_PART_NUMBER_MK64FN1M0VDC12 (value: "n")
 *  "MK64FN1M0VLL12"
 *   Condition: SOC_PART_NUMBER_MK64FN1M0VLL12 (value: "n")
 *  "MK64FN1M0VLQ12"
 *   Condition: SOC_PART_NUMBER_MK64FN1M0VLQ12 (value: "n")
 *  "MK64FN1M0VMD12"
 *   Condition: SOC_PART_NUMBER_MK64FN1M0VMD12 (value: "n")
 *  "MK64FX512VDC12"
 *   Condition: SOC_PART_NUMBER_MK64FX512VDC12 (value: "n")
 *  "MK64FX512VLL12"
 *   Condition: SOC_PART_NUMBER_MK64FX512VLL12 (value: "n")
 *  "MK64FX512VLQ12"
 *   Condition: SOC_PART_NUMBER_MK64FX512VLQ12 (value: "n")
 *  "MK64FX512VMD12"
 *   Condition: SOC_PART_NUMBER_MK64FX512VMD12 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_KINETIS_K6X && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.soc:61