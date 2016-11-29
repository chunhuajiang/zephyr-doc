:orphan:

.. title:: GPIO_QMSI_SS

.. option:: CONFIG_GPIO_QMSI_SS:
.. _CONFIG_GPIO_QMSI_SS:

Enable the GPIO driver found on Intel Microcontroller
boards, on the sensor subsystem, using the QMSI library.



:Symbol:           GPIO_QMSI_SS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI GPIO SS driver" if GPIO && QMSI && ARC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO && QMSI && ARC (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_QUARK_SE_C1000_SS (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:27
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:112