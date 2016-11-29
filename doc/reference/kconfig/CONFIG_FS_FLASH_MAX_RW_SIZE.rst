:orphan:

.. title:: FS_FLASH_MAX_RW_SIZE

.. option:: CONFIG_FS_FLASH_MAX_RW_SIZE:
.. _CONFIG_FS_FLASH_MAX_RW_SIZE:

This is the maximum number of bytes that the
flash_write API can do per invocation.
API.



:Symbol:           FS_FLASH_MAX_RW_SIZE
:Type:             int
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

 *  SPI_FLASH_W25QXXDV_MAX_DATA_LEN (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 DISK_ACCESS_FLASH && FILE_SYSTEM && FS_FAT_FLASH_DISK_W25QXXDV (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:95