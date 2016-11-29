:orphan:

.. title:: ICCM_BASE_ADDRESS

.. option:: CONFIG_ICCM_BASE_ADDRESS:
.. _CONFIG_ICCM_BASE_ADDRESS:

This option specifies the base address of the ICCM on the board.  It is
normally set by the board's defconfig file and the user should generally
avoid modifying it via the menu configuration.



:Symbol:           ICCM_BASE_ADDRESS
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ICCM Base Address"
:Default values:

 *  0xFFFFFFFF (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
 *  0x00000000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:173
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:55
 * ../arch/arc/soc/em11d/Kconfig.defconfig:56
 * ../arch/arc/soc/em7d/Kconfig.defconfig:56
 * ../arch/arc/soc/em9d/Kconfig.defconfig:57