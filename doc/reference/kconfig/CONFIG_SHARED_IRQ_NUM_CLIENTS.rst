:orphan:

.. title:: SHARED_IRQ_NUM_CLIENTS

.. option:: CONFIG_SHARED_IRQ_NUM_CLIENTS:
.. _CONFIG_SHARED_IRQ_NUM_CLIENTS:

Configures the maximum nuber of clients allowed per shared
instance of the shared interrupt driver. To conserve RAM set
this value to the lowest practical value.



:Symbol:           SHARED_IRQ_NUM_CLIENTS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The number of clients per instance" if SHARED_IRQ (value: "n")
:Default values:

 *  5 (value: "n")
 *   Condition: SHARED_IRQ (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/shared_irq/Kconfig:27