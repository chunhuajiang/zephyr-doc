:orphan:

.. title:: TINYDTLS

.. option:: CONFIG_TINYDTLS:
.. _CONFIG_TINYDTLS:

Enable tinyDTLS support so that applications can use it.
This is needed at least in CoAP.



:Symbol:           TINYDTLS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable tinyDTLS support." if NETWORKING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NET_UIP && ER_COAP && ER_COAP_WITH_DTLS (value: "n")
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:493