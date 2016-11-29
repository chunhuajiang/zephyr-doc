:orphan:

.. title:: SOC_FLASH_QMSI_SYS_SIZE

.. option:: CONFIG_SOC_FLASH_QMSI_SYS_SIZE:
.. _CONFIG_SOC_FLASH_QMSI_SYS_SIZE:

Specify system flash size on the quark SOC.



:Symbol:           SOC_FLASH_QMSI_SYS_SIZE
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SOC system flash size" if SOC_FLASH_QMSI (value: "n")
:Default values:

 *  0x8000 (value: "n")
 *   Condition: (none)
 *  0x60000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_FLASH_QMSI && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/flash/Kconfig:115
 * ../arch/x86/soc/intel_quark/quark_d2000/Kconfig.defconfig.series:168
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:226