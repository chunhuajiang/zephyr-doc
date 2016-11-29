:orphan:

.. title:: BOOTLOADER_SRAM_SIZE

.. option:: CONFIG_BOOTLOADER_SRAM_SIZE:
.. _CONFIG_BOOTLOADER_SRAM_SIZE:

This option specifies the amount of SRAM (measure in kB) reserved for
when Zephyr is to act as a bootloader.



:Symbol:           BOOTLOADER_SRAM_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "SRAM reserved for when Zephyr acts as a bootloader" if (!XIP || IS_BOOTLOADER) && ARM (value: "n")
:Default values:

 *  16 (value: "n")
 *   Condition: (!XIP || IS_BOOTLOADER) && ARM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:371