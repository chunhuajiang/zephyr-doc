:orphan:

.. title:: HPET_TIMER_BASE_ADDRESS

.. option:: CONFIG_HPET_TIMER_BASE_ADDRESS:
.. _CONFIG_HPET_TIMER_BASE_ADDRESS:

This options specifies the base address of the HPET timer device.



:Symbol:           HPET_TIMER_BASE_ADDRESS
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HPET Base Address" if HPET_TIMER (value: "n")
:Default values:

 *  0xFED00000 (value: "n")
 *   Condition: HPET_TIMER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/timer/Kconfig:49