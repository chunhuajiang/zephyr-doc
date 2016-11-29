:orphan:

.. title:: PRINTK

.. option:: CONFIG_PRINTK:
.. _CONFIG_PRINTK:

This option directs printk() debugging output to the supported
console device, rather than suppressing the generation
of printk() output entirely. Output is sent immediately, without
any mutual exclusion or buffering.



:Symbol:           PRINTK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Send printk() to console" if CONSOLE_HAS_DRIVER (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: CONSOLE_HAS_DRIVER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BOOT_BANNER (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:184