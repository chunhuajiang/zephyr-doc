:orphan:

.. title:: IPM_CONSOLE_RECEIVER

.. option:: CONFIG_IPM_CONSOLE_RECEIVER:
.. _CONFIG_IPM_CONSOLE_RECEIVER:

Enable the receiving side of IPM console



:Symbol:           IPM_CONSOLE_RECEIVER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Inter-processor Mailbox console receiver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_RING_BUFFER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:138