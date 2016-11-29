:orphan:

.. title:: 15_4_TX_STACK_SIZE

.. option:: CONFIG_15_4_TX_STACK_SIZE:
.. _CONFIG_15_4_TX_STACK_SIZE:

Set the 802.15.4 TX fiber stack size in bytes. The TX fiber
is waiting network packets from IP stack. It then feeds those
to 6LoWPAN stack which compresses and fragments packets before
passing the fragments to 802.15.4 device driver. Note that
this stack needs to be bigger that TX stack because stack is
used to store the fragmented 802.15.4 packets.



:Symbol:           15_4_TX_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Stack size of 802.15.4 TX fiber" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  4096 (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:376