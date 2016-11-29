:orphan:

.. title:: NET_SANITY_TEST

.. option:: CONFIG_NET_SANITY_TEST:
.. _CONFIG_NET_SANITY_TEST:

Enable networking sanity tests. Network sanity test
verification and test report submission will fall under
this config.



:Symbol:           NET_SANITY_TEST
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable networking sanity test" if NETWORKING (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NETWORKING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:576