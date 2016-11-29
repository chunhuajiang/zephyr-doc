:orphan:

.. title:: DCCM_SIZE

.. option:: CONFIG_DCCM_SIZE:
.. _CONFIG_DCCM_SIZE:

This option specifies the size of the DCCM in kB.  It is normally set by
the board's defconfig file and the user should generally avoid modifying
it via the menu configuration.



:Symbol:           DCCM_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DCCM Size in kB"
:Default values:

 *  8 (value: "n")
 *   Condition: (none)
 *  64 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: (none)
 *  128 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:180
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:64
 * ../arch/arc/soc/em11d/Kconfig.defconfig:65
 * ../arch/arc/soc/em7d/Kconfig.defconfig:65
 * ../arch/arc/soc/em9d/Kconfig.defconfig:66