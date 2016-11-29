:orphan:

.. title:: BOARD_HEXIWEAR_K64

.. option:: CONFIG_BOARD_HEXIWEAR_K64:
.. _CONFIG_BOARD_HEXIWEAR_K64:

The configuration item CONFIG_BOARD_HEXIWEAR_K64:

:Symbol:           BOARD_HEXIWEAR_K64
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "NXP Hexiwear K64" if SOC_SERIES_KINETIS_K6X (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_SOC_PART_NUMBER_MK64FN1M0VDC12` if SOC_SERIES_KINETIS_K6X (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../boards/arm/hexiwear_k64/Kconfig.board:18