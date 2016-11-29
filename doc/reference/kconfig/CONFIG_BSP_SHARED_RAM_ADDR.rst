:orphan:

.. title:: BSP_SHARED_RAM_ADDR

.. option:: CONFIG_BSP_SHARED_RAM_ADDR:
.. _CONFIG_BSP_SHARED_RAM_ADDR:

Address of the memory shared between the BSP and the Bootloader in order
to store restore information.



:Symbol:           BSP_SHARED_RAM_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Address of the shared RAM with the QMSI Bootloader" if SYS_POWER_DEEP_SLEEP (value: "n")
:Default values:

 *  0xA8013FFC (value: "n")
 *   Condition: SYS_POWER_DEEP_SLEEP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 && SOC_QUARK_SE_C1000 && X86 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:88