:orphan:

.. title:: SPI_INTEL

.. option:: CONFIG_SPI_INTEL:
.. _CONFIG_SPI_INTEL:

Enable support for Intel's SPI controllers. Such controller
was formelly found on XScale chips. It can be found nowadays
on CEXXXX Intel media controller and Quark CPU (2 of them).




:Symbol:           SPI_INTEL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Intel SPI controller driver" if SPI && CPU_MINUTEIA (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SPI && CPU_MINUTEIA (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SPI && SOC_SERIES_QUARK_X1000 (value: "n")
:Locations:
 * ../drivers/spi/Kconfig:54
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:161