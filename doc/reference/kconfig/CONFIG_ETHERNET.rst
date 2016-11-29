:orphan:

.. title:: ETHERNET

.. option:: CONFIG_ETHERNET:
.. _CONFIG_ETHERNET:

Include Ethernet drivers in system config. This
option enables Ethernet support in the core network
subsystem, but it is necessary to also select a
specific Ethernet device driver.


:Symbol:           ETHERNET
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Ethernet drivers"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:288