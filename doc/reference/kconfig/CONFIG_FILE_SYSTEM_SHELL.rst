:orphan:

.. title:: FILE_SYSTEM_SHELL

.. option:: CONFIG_FILE_SYSTEM_SHELL:
.. _CONFIG_FILE_SYSTEM_SHELL:

This shell provides basic browsing of the contents of the
file system.



:Symbol:           FILE_SYSTEM_SHELL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable file system shell" if ENABLE_SHELL (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 FILE_SYSTEM (value: "n")
:Locations:
 * ../subsys/fs/Kconfig:27