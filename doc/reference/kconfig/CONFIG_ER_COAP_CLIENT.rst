:orphan:

.. title:: ER_COAP_CLIENT

.. option:: CONFIG_ER_COAP_CLIENT:
.. _CONFIG_ER_COAP_CLIENT:

Compile in client CoAP support.



:Symbol:           ER_COAP_CLIENT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable CoAP client support" if ER_COAP (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ER_COAP (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:545