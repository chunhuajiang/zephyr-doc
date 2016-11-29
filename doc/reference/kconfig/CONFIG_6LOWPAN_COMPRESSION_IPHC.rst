:orphan:

.. title:: 6LOWPAN_COMPRESSION_IPHC

.. option:: CONFIG_6LOWPAN_COMPRESSION_IPHC:
.. _CONFIG_6LOWPAN_COMPRESSION_IPHC:

IP header compression


:Symbol:           6LOWPAN_COMPRESSION_IPHC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "IP header compression"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NETWORKING_WITH_IPV6 && NETWORKING && NET_UIP && NETWORKING_WITH_BT (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:487