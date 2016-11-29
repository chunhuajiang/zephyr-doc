:orphan:

.. title:: IP_TX_STACK_SIZE

.. option:: CONFIG_IP_TX_STACK_SIZE:
.. _CONFIG_IP_TX_STACK_SIZE:

Set the TX fiber stack size in bytes. The TX fiber is waiting
data from application. It will then validate the data and push
it to network driver to be sent out.



:Symbol:           IP_TX_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TX fiber stack size"
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
 * ../net/ip/Kconfig:71