:orphan:

.. title:: PINMUX_INIT_PRIORITY

.. option:: CONFIG_PINMUX_INIT_PRIORITY:
.. _CONFIG_PINMUX_INIT_PRIORITY:

Pinmux driver initialization priority.
Pinmux driver almost certainly should be initialized before the
rest of hardware devices (which may need specific pins already
configured for them), and usually after generic GPIO drivers.
Thus, its priority should be between KERNEL_INIT_PRIORITY_DEFAULT
and KERNEL_INIT_PRIORITY_DEVICE. There are exceptions to this
rule for particular boards. Don't change this value unless you
know what you are doing.



:Symbol:           PINMUX_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if PINMUX (value: "n")
:Default values:

 *  45 (value: "n")
 *   Condition: PINMUX (value: "n")
 *  80 (value: "n")
 *   Condition: PINMUX (value: "n")
 *  80 (value: "n")
 *   Condition: PINMUX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/pinmux/Kconfig:37
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:268
 * ../boards/x86/galileo/Kconfig.defconfig:131