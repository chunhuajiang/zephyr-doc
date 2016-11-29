:orphan:

.. title:: NETWORK_LOOPBACK_TEST_COUNT

.. option:: CONFIG_NETWORK_LOOPBACK_TEST_COUNT:
.. _CONFIG_NETWORK_LOOPBACK_TEST_COUNT:

If set to 0, then the loopback test runs forever.



:Symbol:           NETWORK_LOOPBACK_TEST_COUNT
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "How many packets the loopback test passes" if NETWORKING_WITH_LOOPBACK (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: NETWORKING_WITH_LOOPBACK (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:266