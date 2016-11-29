:orphan:

.. title:: RPL_PROBING

.. option:: CONFIG_RPL_PROBING:
.. _CONFIG_RPL_PROBING:

Enable RPL probing support. When enabled, probes will be sent
periodically to keep parent link estimates up to date.



:Symbol:           RPL_PROBING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable RPL probing" if NETWORKING_WITH_RPL (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING_WITH_RPL (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:218