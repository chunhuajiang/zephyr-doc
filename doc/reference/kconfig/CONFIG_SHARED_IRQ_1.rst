:orphan:

.. title:: SHARED_IRQ_1

.. option:: CONFIG_SHARED_IRQ_1:
.. _CONFIG_SHARED_IRQ_1:

Provide an instance of the shared interrupt driver when system
configuration requires that multiple devices share an interrupt.



:Symbol:           SHARED_IRQ_1
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Shared interrupt instance 1" if SHARED_IRQ (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/shared_irq/Kconfig:98