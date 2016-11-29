:orphan:

.. title:: BLUETOOTH_ATT_REQ_COUNT

.. option:: CONFIG_BLUETOOTH_ATT_REQ_COUNT:
.. _CONFIG_BLUETOOTH_ATT_REQ_COUNT:

Number of outgoing buffers available for ATT requests, this controls
how many requests can be queued without blocking.



:Symbol:           BLUETOOTH_ATT_REQ_COUNT
:Type:             int
:Value:            "1"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [1, 64]
:Prompts:

 *  "Number of ATT request buffers"
:Default values:

 *  BLUETOOTH_MAX_CONN (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_HCI_HOST && BLUETOOTH_CONN (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:159