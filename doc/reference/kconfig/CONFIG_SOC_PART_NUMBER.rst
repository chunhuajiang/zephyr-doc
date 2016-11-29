:orphan:

.. title:: SOC_PART_NUMBER

.. option:: CONFIG_SOC_PART_NUMBER:
.. _CONFIG_SOC_PART_NUMBER:

This string holds the full part number of the SoC. It is a hidden option
that you should not set directly. The part number selection choice defines
the default value for this string.



:Symbol:           SOC_PART_NUMBER
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

 *  SOC_PART_NUMBER_KINETIS_K6X (value: "")
 *   Condition: SOC_SERIES_KINETIS_K6X (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/Kconfig:31