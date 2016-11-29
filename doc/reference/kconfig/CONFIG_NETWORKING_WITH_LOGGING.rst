:orphan:

.. title:: NETWORKING_WITH_LOGGING

.. option:: CONFIG_NETWORKING_WITH_LOGGING:
.. _CONFIG_NETWORKING_WITH_LOGGING:

Enable logging in various parts of the network stack.



:Symbol:           NETWORKING_WITH_LOGGING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable network stack logging"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_STDOUT_CONSOLE`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:19