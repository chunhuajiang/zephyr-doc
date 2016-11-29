:orphan:

.. title:: GPIO_QMSI_SS_0

.. option:: CONFIG_GPIO_QMSI_SS_0:
.. _CONFIG_GPIO_QMSI_SS_0:

Include support for the GPIO SS port 0 using QMSI.



:Symbol:           GPIO_QMSI_SS_0
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI GPIO SS block 0"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_QUARK_SE_C1000_SS && GPIO_QMSI_SS (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:93
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:117