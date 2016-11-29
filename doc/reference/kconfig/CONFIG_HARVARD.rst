:orphan:

.. title:: HARVARD

.. option:: CONFIG_HARVARD:
.. _CONFIG_HARVARD:

The ARC CPU can be configured to have two busses;
one for instruction fetching and another that serves as a data bus.



:Symbol:           HARVARD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Harvard Architecture"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:158
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:38
 * ../arch/arc/soc/em11d/Kconfig.defconfig:40
 * ../arch/arc/soc/em7d/Kconfig.defconfig:40
 * ../arch/arc/soc/em9d/Kconfig.defconfig:40