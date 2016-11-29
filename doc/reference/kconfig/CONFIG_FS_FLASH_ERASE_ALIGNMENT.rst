:orphan:

.. title:: FS_FLASH_ERASE_ALIGNMENT

.. option:: CONFIG_FS_FLASH_ERASE_ALIGNMENT:
.. _CONFIG_FS_FLASH_ERASE_ALIGNMENT:

This is the start address alignment required by
the flash component.



:Symbol:           FS_FLASH_ERASE_ALIGNMENT
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  0x1000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 DISK_ACCESS_FLASH && FILE_SYSTEM && FS_FAT_FLASH_DISK_W25QXXDV (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:103