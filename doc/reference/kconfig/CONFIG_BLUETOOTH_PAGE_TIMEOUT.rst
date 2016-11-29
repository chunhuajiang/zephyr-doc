:orphan:

.. title:: BLUETOOTH_PAGE_TIMEOUT

.. option:: CONFIG_BLUETOOTH_PAGE_TIMEOUT:
.. _CONFIG_BLUETOOTH_PAGE_TIMEOUT:

This option sets the page timeout value. Value is selected as
(N * 0.625) ms.



:Symbol:           BLUETOOTH_PAGE_TIMEOUT
:Type:             hex
:Value:            "0x1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0x0001, 0xffff]
:Prompts:

 *  "Bluetooth Page Timeout"
:Default values:

 *  0x2000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_BREDR (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:467