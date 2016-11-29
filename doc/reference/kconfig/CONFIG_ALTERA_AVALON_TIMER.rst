:orphan:

.. title:: ALTERA_AVALON_TIMER

.. option:: CONFIG_ALTERA_AVALON_TIMER:
.. _CONFIG_ALTERA_AVALON_TIMER:

This module implements a kernel device driver for the Altera Avalon
Interval Timer as described in the Embedded IP documentation, for use
with Nios II and possibly other Altera soft CPUs. It provides the
standard "system clock driver" interfaces.



:Symbol:           ALTERA_AVALON_TIMER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Altera Avalon Interval Timer" if NIOS2 (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: NIOS2 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:142