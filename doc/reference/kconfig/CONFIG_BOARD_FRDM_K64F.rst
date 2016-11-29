:orphan:

.. title:: BOARD_FRDM_K64F

.. option:: CONFIG_BOARD_FRDM_K64F:
.. _CONFIG_BOARD_FRDM_K64F:

The configuration item CONFIG_BOARD_FRDM_K64F:

:Symbol:           BOARD_FRDM_K64F
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale FRDM-K64F" if SOC_SERIES_KINETIS_K6X (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_SOC_PART_NUMBER_MK64FN1M0VLL12` if SOC_SERIES_KINETIS_K6X (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../boards/arm/frdm_k64f/Kconfig.board:2