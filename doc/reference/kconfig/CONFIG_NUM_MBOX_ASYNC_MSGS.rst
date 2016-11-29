:orphan:

.. title:: NUM_MBOX_ASYNC_MSGS

.. option:: CONFIG_NUM_MBOX_ASYNC_MSGS:
.. _CONFIG_NUM_MBOX_ASYNC_MSGS:

This option specifies the total number of asynchronous mailbox
messages that can exist simultaneously, across all mailboxes
in the system.

Setting this option to 0 disables support for asynchronous
mailbox messages.



:Symbol:           NUM_MBOX_ASYNC_MSGS
:Type:             int
:Value:            "10"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  ""
:Default values:

 *  10 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:218