:orphan:

.. title:: FS_FAT_FLASH_DISK_W25QXXDV

.. option:: CONFIG_FS_FAT_FLASH_DISK_W25QXXDV:
.. _CONFIG_FS_FAT_FLASH_DISK_W25QXXDV:

Enables to use the W25QXXDV as the storage media
for the file system.



:Symbol:           FS_FAT_FLASH_DISK_W25QXXDV
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "W25QXXDV flash component"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 DISK_ACCESS_FLASH && FILE_SYSTEM (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:74