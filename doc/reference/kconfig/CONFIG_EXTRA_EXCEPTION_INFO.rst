:orphan:

.. title:: EXTRA_EXCEPTION_INFO

.. option:: CONFIG_EXTRA_EXCEPTION_INFO:
.. _CONFIG_EXTRA_EXCEPTION_INFO:

Have exceptions print additional useful debugging information in
human-readable form, at the expense of code size. For example,
the cause code for an exception will be supplemented by a string
describing what that cause code means.



:Symbol:           EXTRA_EXCEPTION_INFO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Extra exception debug information"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NIOS2 (value: "n")
:Locations:
 * ../arch/nios2/Kconfig:79