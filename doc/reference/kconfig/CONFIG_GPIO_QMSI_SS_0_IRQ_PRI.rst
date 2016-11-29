:orphan:

.. title:: GPIO_QMSI_SS_0_IRQ_PRI

.. option:: CONFIG_GPIO_QMSI_SS_0_IRQ_PRI:
.. _CONFIG_GPIO_QMSI_SS_0_IRQ_PRI:

IRQ priority



:Symbol:           GPIO_QMSI_SS_0_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Controller interrupt priority" if GPIO_QMSI_SS_0 (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_QUARK_SE_C1000_SS && GPIO_QMSI_SS && GPIO_QMSI_SS_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:104
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:122