:orphan:

.. title:: NETWORKING_WITH_15_4_RDC_SIMPLE

.. option:: CONFIG_NETWORKING_WITH_15_4_RDC_SIMPLE:
.. _CONFIG_NETWORKING_WITH_15_4_RDC_SIMPLE:

Enable simplerdc driver.


:Symbol:           NETWORKING_WITH_15_4_RDC_SIMPLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "simplerdc driver"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:353