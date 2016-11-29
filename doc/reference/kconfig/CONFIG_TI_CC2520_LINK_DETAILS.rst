:orphan:

.. title:: TI_CC2520_LINK_DETAILS

.. option:: CONFIG_TI_CC2520_LINK_DETAILS:
.. _CONFIG_TI_CC2520_LINK_DETAILS:

If necessary, it will be possible to grab link and RSSI information
from the packet footer and forward them to the above stack.



:Symbol:           TI_CC2520_LINK_DETAILS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Forward RSSI and link information on reception to upper stack"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_TI_CC2520_AUTO_CRC`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING_WITH_15_4_TI_CC2520 && NETWORKING_WITH_15_4 (value: "n")
:Locations:
 * ../drivers/ieee802154/Kconfig:112