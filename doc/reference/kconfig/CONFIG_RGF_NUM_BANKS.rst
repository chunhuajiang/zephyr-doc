:orphan:

.. title:: RGF_NUM_BANKS

.. option:: CONFIG_RGF_NUM_BANKS:
.. _CONFIG_RGF_NUM_BANKS:

The ARC CPU can be configured to have more than one register
bank. If fast interrupts are supported (FIRQ), the 2nd
register bank, in the set, will be used by FIRQ interrupts.
If fast interrupts are supported but there is only 1
register bank, the fast interrupt handler must save
and restore general purpose regsiters.



:Symbol:           RGF_NUM_BANKS
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 2]
:Prompts:

 *  "Number of General Purpose Register Banks" if CPU_ARCV2 (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: CPU_ARCV2 (value: "n")
 *  2 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
 *  1 (value: "n")
 *   Condition: (none)
 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_EM9D (value: "n")
:Locations:
 * ../arch/arc/Kconfig:99
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:32
 * ../arch/arc/soc/em11d/Kconfig.defconfig:34
 * ../arch/arc/soc/em7d/Kconfig.defconfig:34
 * ../arch/arc/soc/em9d/Kconfig.defconfig:34