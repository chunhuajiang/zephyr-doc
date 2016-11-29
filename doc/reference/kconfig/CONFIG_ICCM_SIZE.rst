:orphan:

.. title:: ICCM_SIZE

.. option:: CONFIG_ICCM_SIZE:
.. _CONFIG_ICCM_SIZE:

This option specifies the size of the ICCM in kB.  It is normally set by
the board's defconfig file and the user should generally avoid modifying
it via the menu configuration.



:Symbol:           ICCM_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ICCM Size in kB"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: (none)
 *  256 (value: "n")
 *   Condition: (none)
 *  256 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:166
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:58
 * ../arch/arc/soc/em11d/Kconfig.defconfig:59
 * ../arch/arc/soc/em7d/Kconfig.defconfig:59
 * ../arch/arc/soc/em9d/Kconfig.defconfig:60