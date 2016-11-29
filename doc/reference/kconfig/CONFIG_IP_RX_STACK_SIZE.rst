:orphan:

.. title:: IP_RX_STACK_SIZE

.. option:: CONFIG_IP_RX_STACK_SIZE:
.. _CONFIG_IP_RX_STACK_SIZE:

Set the RX fiber stack size in bytes. The RX fiber is waiting
network packets from lower level bearers. It will then run the
packet through IP stack which validates the packet and passes
it eventually to application.



:Symbol:           IP_RX_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "RX fiber stack size"
:Default values:

 *  1024 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:62