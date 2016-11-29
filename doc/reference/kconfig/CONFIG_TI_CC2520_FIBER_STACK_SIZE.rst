:orphan:

.. title:: TI_CC2520_FIBER_STACK_SIZE

.. option:: CONFIG_TI_CC2520_FIBER_STACK_SIZE:
.. _CONFIG_TI_CC2520_FIBER_STACK_SIZE:

This option sets the driver's stack size for its internal fiber.
The default value should be sufficient, but it case it prooves to be
a too little, this option makes it easy to play with the size.



:Symbol:           TI_CC2520_FIBER_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver's internal fiber stack size"
:Default values:

 *  640 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:88