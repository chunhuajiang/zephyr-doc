:orphan:

.. title:: INCLUDE_RESET_VECTOR

.. option:: CONFIG_INCLUDE_RESET_VECTOR:
.. _CONFIG_INCLUDE_RESET_VECTOR:

Include the reset vector stub, which enables instruction/data caches
and then jumps to __start. This code is typically located at the very
beginning of flash memory. You may need to omit this if using the
nios2-download tool since it refuses to load data anywhere other than
RAM.



:Symbol:           INCLUDE_RESET_VECTOR
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Include Reset vector"
:Default values:

 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NIOS2 (value: "n")
:Locations:
 * ../arch/nios2/Kconfig:69