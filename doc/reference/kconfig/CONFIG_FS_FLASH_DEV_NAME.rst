:orphan:

.. title:: FS_FLASH_DEV_NAME

.. option:: CONFIG_FS_FLASH_DEV_NAME:
.. _CONFIG_FS_FLASH_DEV_NAME:

The configuration item CONFIG_FS_FLASH_DEV_NAME:

:Symbol:           FS_FLASH_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "File system flash storage device name" if SPI_FLASH_W25QXXDV (value: "n")
:Default values:

 *  SPI_FLASH_W25QXXDV_DRV_NAME (value: "")
 *   Condition: SPI_FLASH_W25QXXDV (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 DISK_ACCESS_FLASH && FILE_SYSTEM && FS_FAT_FLASH_DISK_W25QXXDV (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:82