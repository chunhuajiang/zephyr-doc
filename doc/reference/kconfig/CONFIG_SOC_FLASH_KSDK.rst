:orphan:

.. title:: SOC_FLASH_KSDK

.. option:: CONFIG_SOC_FLASH_KSDK:
.. _CONFIG_SOC_FLASH_KSDK:

Enables the KSDK flash shim driver.
WARNING: This driver will disable the system interrupts for
the duration of the flash erase/write operations. This will
have an impact on the overall system performance - whether
this is acceptable or not will depend on the use case.



:Symbol:           SOC_FLASH_KSDK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "KSDK flash shim driver" if FLASH && HAS_KSDK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: FLASH && HAS_KSDK (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && FLASH (value: "n")
:Locations:
 * ../drivers/flash/Kconfig:135
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:82