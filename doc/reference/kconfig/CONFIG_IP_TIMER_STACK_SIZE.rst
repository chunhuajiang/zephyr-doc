:orphan:

.. title:: IP_TIMER_STACK_SIZE

.. option:: CONFIG_IP_TIMER_STACK_SIZE:
.. _CONFIG_IP_TIMER_STACK_SIZE:

Set the timer fiber stack size in bytes. The timer fiber is
responsible for handling re-transmissions and periodic network
packet sending like IPv6 router solicitations.



:Symbol:           IP_TIMER_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Timer fiber stack size"
:Default values:

 *  1536 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:79