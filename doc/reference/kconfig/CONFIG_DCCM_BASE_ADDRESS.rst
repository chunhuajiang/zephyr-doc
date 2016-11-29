:orphan:

.. title:: DCCM_BASE_ADDRESS

.. option:: CONFIG_DCCM_BASE_ADDRESS:
.. _CONFIG_DCCM_BASE_ADDRESS:

This option specifies the base address of the DCCM on the board.  It is
normally set by the board's defconfig file and the user should generally
avoid modifying it via the menu configuration.



:Symbol:           DCCM_BASE_ADDRESS
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DCCM Base Address"
:Default values:

 *  0x80000000 (value: "n")
 *   Condition: (none)
 *  0x80000000 (value: "n")
 *   Condition: (none)
 *  0x80000000 (value: "n")
 *   Condition: (none)
 *  0x80000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:187
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:61
 * ../arch/arc/soc/em11d/Kconfig.defconfig:62
 * ../arch/arc/soc/em7d/Kconfig.defconfig:62
 * ../arch/arc/soc/em9d/Kconfig.defconfig:63