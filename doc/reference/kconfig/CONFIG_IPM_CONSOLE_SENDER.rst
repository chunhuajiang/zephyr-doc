:orphan:

.. title:: IPM_CONSOLE_SENDER

.. option:: CONFIG_IPM_CONSOLE_SENDER:
.. _CONFIG_IPM_CONSOLE_SENDER:

Enable the sending side of IPM console



:Symbol:           IPM_CONSOLE_SENDER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Inter-processor Mailbox console sender"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_CONSOLE_HAS_DRIVER`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:130