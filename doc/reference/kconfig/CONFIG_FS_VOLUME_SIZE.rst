:orphan:

.. title:: FS_VOLUME_SIZE

.. option:: CONFIG_FS_VOLUME_SIZE:
.. _CONFIG_FS_VOLUME_SIZE:

This is the file system volume size in bytes.



:Symbol:           FS_VOLUME_SIZE
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

 *  0x18000 (value: "n")
 *   Condition: DISK_ACCESS_RAM (value: "n")
 *  0x200000 (value: "n")
 *   Condition: FS_FAT_FLASH_DISK_W25QXXDV (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FILE_SYSTEM (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:57