:orphan:

.. title:: NET_TESTING

.. option:: CONFIG_NET_TESTING:
.. _CONFIG_NET_TESTING:

Setup the network stack such a way that it is suitable for
testing with Qemu and slip.



:Symbol:           NET_TESTING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable network testing setup" if NETWORKING (value: "n")
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
 * ../net/ip/Kconfig:594