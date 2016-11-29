:orphan:

.. title:: BSP_SHARED_RAM_SIZE

.. option:: CONFIG_BSP_SHARED_RAM_SIZE:
.. _CONFIG_BSP_SHARED_RAM_SIZE:

Size of the memory shared between the BSP and the Bootloader in order
to store restore information.



:Symbol:           BSP_SHARED_RAM_SIZE
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Size of the shared RAM with the QMSI Bootloader" if SYS_POWER_DEEP_SLEEP (value: "n")
:Default values:

 *  0x4 (value: "n")
 *   Condition: SYS_POWER_DEEP_SLEEP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:96