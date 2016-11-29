:orphan:

.. title:: GDT_DYNAMIC

.. option:: CONFIG_GDT_DYNAMIC:
.. _CONFIG_GDT_DYNAMIC:

This option stores the GDT in RAM instead of ROM, so that it may
be modified at runtime at the expense of some memory.



:Symbol:           GDT_DYNAMIC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Store GDT in RAM so that it can be modified" if SET_GDT (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: SET_GDT (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:106