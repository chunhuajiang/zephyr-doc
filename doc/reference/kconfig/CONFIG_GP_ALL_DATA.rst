:orphan:

.. title:: GP_ALL_DATA

.. option:: CONFIG_GP_ALL_DATA:
.. _CONFIG_GP_ALL_DATA:

Use GP relative access for all data in the program, not just
small data. Use this if your board has 64K or less of RAM.



:Symbol:           GP_ALL_DATA
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "All data global pointer references"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NIOS2 (value: "n")
:Locations:
 * ../arch/nios2/Kconfig:112