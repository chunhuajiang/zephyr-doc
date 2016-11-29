:orphan:

.. title:: 15_4_RX_STACK_SIZE

.. option:: CONFIG_15_4_RX_STACK_SIZE:
.. _CONFIG_15_4_RX_STACK_SIZE:

Set the 802.15.4 RX fiber stack size in bytes. The RX fiber
is waiting network packets from 802.15.4 device driver.
It will then run the packet through 6LoWPAN stack which
uncompresses and de-fragments the packet and passes those to
upper layers.



:Symbol:           15_4_RX_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Stack size of 802.15.4 RX fiber" if NETWORKING_WITH_15_4 (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: NETWORKING_WITH_15_4 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:365