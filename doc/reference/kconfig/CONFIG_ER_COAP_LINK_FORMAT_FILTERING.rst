:orphan:

.. title:: ER_COAP_LINK_FORMAT_FILTERING

.. option:: CONFIG_ER_COAP_LINK_FORMAT_FILTERING:
.. _CONFIG_ER_COAP_LINK_FORMAT_FILTERING:

Make CoAP engine support link format filters.



:Symbol:           ER_COAP_LINK_FORMAT_FILTERING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable link format filtering"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_MINIMAL_LIBC_EXTENDED`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:529