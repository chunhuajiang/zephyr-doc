:orphan:

.. title:: BLUETOOTH_MAX_EVT_LEN

.. option:: CONFIG_BLUETOOTH_MAX_EVT_LEN:
.. _CONFIG_BLUETOOTH_MAX_EVT_LEN:

Maximum size of each HCI event buffer. E.g. one big event
for LE is the Command Complete for Read Local Supported
Commands. It is a 3 byte Command Complete header + 65 byte
return parameters = 68 bytes in total.



:Symbol:           BLUETOOTH_MAX_EVT_LEN
:Type:             int
:Value:            "68"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [68, 255]
:Prompts:

 *  "Maximum supported HCI event length"
:Default values:

 *  68 (value: "n")
 *   Condition: (none)
 *  255 (value: "n")
 *   Condition: BLUETOOTH_BREDR (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:64