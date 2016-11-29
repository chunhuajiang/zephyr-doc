:orphan:

.. title:: GPIO_QMSI_SS_1

.. option:: CONFIG_GPIO_QMSI_SS_1:
.. _CONFIG_GPIO_QMSI_SS_1:

Include support for the GPIO SS port 1 using QMSI.



:Symbol:           GPIO_QMSI_SS_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI GPIO SS block 1"
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
 * ../drivers/gpio/Kconfig.qmsi:110
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:127