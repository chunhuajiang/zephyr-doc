:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_COAP_INTERNAL

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_COAP_INTERNAL:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_COAP_INTERNAL:

Enables CoAP internals output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_COAP_INTERNAL
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug CoAP internals" if ER_COAP (value: "n")
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
 * ../net/ip/Kconfig.debug:243