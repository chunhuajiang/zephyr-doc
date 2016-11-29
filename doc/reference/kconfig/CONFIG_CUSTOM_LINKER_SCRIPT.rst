:orphan:

.. title:: CUSTOM_LINKER_SCRIPT

.. option:: CONFIG_CUSTOM_LINKER_SCRIPT:
.. _CONFIG_CUSTOM_LINKER_SCRIPT:

Path to the linker script to be used instead of the one define by the
board.

The linker script must be based on a version provided by Zephyr since
the kernel can expect a certain layout/certain regions.

This is useful when an application needs to add sections into the
linker script and avoid having to change the script provided by
Zephyr.



:Symbol:           CUSTOM_LINKER_SCRIPT
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Path to custom linker script" if HAVE_CUSTOM_LINKER_SCRIPT (value: "n")
:Default values:

 *  ""
 *   Condition: HAVE_CUSTOM_LINKER_SCRIPT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:41