:orphan:

.. title:: SPI_QMSI

.. option:: CONFIG_SPI_QMSI:
.. _CONFIG_SPI_QMSI:

SPI driver implementation using QMSI library. QMSI is the
Quark Microcontroller Software Interface, providing a common
interface to the Quark family of microcontrollers.



:Symbol:           SPI_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI driver for SPI controller" if SPI && QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI && QMSI (value: "n")
 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:29
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:159
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:155