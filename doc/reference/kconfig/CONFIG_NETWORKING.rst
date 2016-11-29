:orphan:

.. title:: NETWORKING

.. option:: CONFIG_NETWORKING:
.. _CONFIG_NETWORKING:

This option enabled generic networking support.



:Symbol:           NETWORKING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Generic networking support"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_NANO_TIMEOUTS`
 *  :option:`CONFIG_NANO_TIMERS`
 *  :option:`CONFIG_NET_BUF`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../net/ip/Kconfig:23