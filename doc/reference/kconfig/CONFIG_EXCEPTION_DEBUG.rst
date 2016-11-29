:orphan:

.. title:: EXCEPTION_DEBUG

.. option:: CONFIG_EXCEPTION_DEBUG:
.. _CONFIG_EXCEPTION_DEBUG:

Install handlers for various CPU exception/trap vectors to
make debugging them easier, at a small expense in code size.
This prints out the specific exception vector and any associated
error codes.



:Symbol:           EXCEPTION_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Unhandled exception debugging" if PRINTK (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: PRINTK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/core/Kconfig:28