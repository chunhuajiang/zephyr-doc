:orphan:

.. title:: SPI_QMSI_SS

.. option:: CONFIG_SPI_QMSI_SS:
.. _CONFIG_SPI_QMSI_SS:

SPI driver implementation using QMSI library. This instance is
for the Sensor Subsystem.



:Symbol:           SPI_QMSI_SS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI driver for SPI controller on Sensor Subsystem" if SPI && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI && QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_QUARK_SE_C1000_SS (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:38
 * ../arch/arc/soc/quark_se_c1000_ss/Kconfig.defconfig:218