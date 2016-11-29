:orphan:

.. title:: NETWORKING_WITH_15_4_TI_CC2520

.. option:: CONFIG_NETWORKING_WITH_15_4_TI_CC2520:
.. _CONFIG_NETWORKING_WITH_15_4_TI_CC2520:

Enable Texas Instruments CC2520 802.15.4 radio driver.



:Symbol:           NETWORKING_WITH_15_4_TI_CC2520
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TI CC2520"
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_TEST_RANDOM_GENERATOR`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:424