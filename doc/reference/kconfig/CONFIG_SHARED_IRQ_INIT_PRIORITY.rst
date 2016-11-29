:orphan:

.. title:: SHARED_IRQ_INIT_PRIORITY

.. option:: CONFIG_SHARED_IRQ_INIT_PRIORITY:
.. _CONFIG_SHARED_IRQ_INIT_PRIORITY:

Shared IRQ are initialized on POST_KERNEL init level. They
have to be initialized before any device that uses them.



:Symbol:           SHARED_IRQ_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared IRQ init priority" if SHARED_IRQ (value: "n")
:Default values:

 *  45 (value: "n")
 *   Condition: SHARED_IRQ (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/shared_irq/Kconfig:37