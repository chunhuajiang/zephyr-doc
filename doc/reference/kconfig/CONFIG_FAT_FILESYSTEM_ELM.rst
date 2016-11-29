:orphan:

.. title:: FAT_FILESYSTEM_ELM

.. option:: CONFIG_FAT_FILESYSTEM_ELM:
.. _CONFIG_FAT_FILESYSTEM_ELM:

Use the ELM FAT File system implementation.


:Symbol:           FAT_FILESYSTEM_ELM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ELM FAT File System" if FILE_SYSTEM_FAT (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: FILE_SYSTEM_FAT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/fs/fat/Kconfig:2