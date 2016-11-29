:orphan:

.. title:: NETWORK_IP_STACK_DEBUG_COAP_ENGINE

.. option:: CONFIG_NETWORK_IP_STACK_DEBUG_COAP_ENGINE:
.. _CONFIG_NETWORK_IP_STACK_DEBUG_COAP_ENGINE:

Enables CoAP engine output debug messages



:Symbol:           NETWORK_IP_STACK_DEBUG_COAP_ENGINE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Debug CoAP engine" if ER_COAP (value: "n")
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
 * ../net/ip/Kconfig.debug:229