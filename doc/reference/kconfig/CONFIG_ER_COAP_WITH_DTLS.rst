:orphan:

.. title:: ER_COAP_WITH_DTLS

.. option:: CONFIG_ER_COAP_WITH_DTLS:
.. _CONFIG_ER_COAP_WITH_DTLS:

Make CoAP engine use DTLS. Note that if you activate DTLS, you
are not able to send or receive non-DTLS CoAP messages, and
vice versa.



:Symbol:           ER_COAP_WITH_DTLS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use DTLS in CoAP" if ER_COAP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ER_COAP (value: "n")
:Selects:

 *  :option:`CONFIG_TINYDTLS` if ER_COAP (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:518