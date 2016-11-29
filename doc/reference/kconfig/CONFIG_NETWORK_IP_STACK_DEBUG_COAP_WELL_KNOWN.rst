:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_COAP_WELL_KNOWN

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_COAP_WELL_KNOWN:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_COAP_WELL_KNOWN:

Enables CoAP resource well known core ouput debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_COAP_WELL_KNOWN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug CoAP well known core" if ER_COAP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ER_COAP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (NETWORKING_WITH_LOGGING || NET_LOG) && NETWORKING (value: "n")
:Locations:
 * ../net/ip/Kconfig.debug:257