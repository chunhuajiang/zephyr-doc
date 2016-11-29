:orphan:

.. title:: BLUETOOTH_MAX_CMD_LEN

.. option:: CONFIG_BLUETOOTH_MAX_CMD_LEN:
.. _CONFIG_BLUETOOTH_MAX_CMD_LEN:

Maximum length of each HCI command.



:Symbol:           BLUETOOTH_MAX_CMD_LEN
:Type:             int
:Value:            "64"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [64, 255]
 *  [255, 255] if BLUETOOTH_BREDR (value: "n")
:Prompts:

 *  "Maximum supported HCI command length"
:Default values:

 *  64 (value: "n")
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
 * ../subsys/bluetooth/host/Kconfig:44