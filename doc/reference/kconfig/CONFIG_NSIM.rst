:orphan:

.. title:: NSIM

.. option:: CONFIG_NSIM:
.. _CONFIG_NSIM:

For running on nSIM simulator.

a) Uses non-XIP to run in RAM.
b) Linked at address 0x4000 with 0x4000 of RAM so that it works with
   a pc_size of 16 (default).



:Symbol:           NSIM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Running on the MetaWare nSIM simulator"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 ARC (value: "n")
:Locations:
 * ../arch/arc/Kconfig:58