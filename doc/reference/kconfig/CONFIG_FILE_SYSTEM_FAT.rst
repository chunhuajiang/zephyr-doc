:orphan:

.. title:: FILE_SYSTEM_FAT

.. option:: CONFIG_FILE_SYSTEM_FAT:
.. _CONFIG_FILE_SYSTEM_FAT:

Enables FAT file system support.



:Symbol:           FILE_SYSTEM_FAT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "FAT file system support"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FILE_SYSTEM (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:34