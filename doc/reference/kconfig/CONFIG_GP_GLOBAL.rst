:orphan:

.. title:: GP_GLOBAL

.. option:: CONFIG_GP_GLOBAL:
.. _CONFIG_GP_GLOBAL:

Use global pointer relative offsets for small globals declared
anywhere in the executable. Note that if any small globals that are put
in alternate sections (such as _k_task_list_ptr in the microkernel)
they must be declared in headers with proper __attribute__((section)) or
the linker will error out.



:Symbol:           GP_GLOBAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Global data global pointer references"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NIOS2 (value: "n")
:Locations:
 * ../arch/nios2/Kconfig:103