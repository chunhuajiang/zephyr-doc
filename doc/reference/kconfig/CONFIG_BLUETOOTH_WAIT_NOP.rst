:orphan:

.. title:: BLUETOOTH_WAIT_NOP

.. option:: CONFIG_BLUETOOTH_WAIT_NOP:
.. _CONFIG_BLUETOOTH_WAIT_NOP:

Some controllers emit a Command Complete event for the NOP
opcode to indicate that they're ready to receive commands.
This option should be selected if the controller used
exhibits such behavior.



:Symbol:           BLUETOOTH_WAIT_NOP
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Wait for "NOP" Command Complete event during init" if BLUETOOTH_HCI (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH (value: "n")
:Locations:
 * ../drivers/bluetooth/Kconfig:42