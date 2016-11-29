:orphan:

.. title:: IOAPIC_MASK_RTE

.. option:: CONFIG_IOAPIC_MASK_RTE:
.. _CONFIG_IOAPIC_MASK_RTE:

At boot, mask all IOAPIC RTEs if they may be in an undefined state.
You don't need this if the RTEs are either all guaranteed to be masked
when the OS starts up, or a previous boot stage has done some IOAPIC
configuration that needs to be preserved.



:Symbol:           IOAPIC_MASK_RTE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Mask out RTE entries on boot" if IOAPIC (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: IOAPIC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/interrupt_controller/Kconfig:94