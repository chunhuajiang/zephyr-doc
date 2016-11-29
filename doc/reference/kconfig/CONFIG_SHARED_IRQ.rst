:orphan:

.. title:: SHARED_IRQ

.. option:: CONFIG_SHARED_IRQ:
.. _CONFIG_SHARED_IRQ:

Include shared interrupt support in system. Shared interrupt
support is NOT required in most systems. If in doubt answer no.



:Symbol:           SHARED_IRQ
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared interrupt driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/shared_irq/Kconfig:19
 * ../boards/x86/galileo/Kconfig.defconfig:25