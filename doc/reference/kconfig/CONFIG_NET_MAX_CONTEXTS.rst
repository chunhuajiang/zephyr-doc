:orphan:

.. title:: NET_MAX_CONTEXTS

.. option:: CONFIG_NET_MAX_CONTEXTS:
.. _CONFIG_NET_MAX_CONTEXTS:

The network context is similar concept as network socket.
It defines a network endpoint and number of context depends
on application usage.



:Symbol:           NET_MAX_CONTEXTS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "How many network context to use"
:Default values:

 *  2 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:87