:orphan:

.. title:: GDB_REMOTE_SERIAL_EXT_NOTIF_PREFIX_STR

.. option:: CONFIG_GDB_REMOTE_SERIAL_EXT_NOTIF_PREFIX_STR:
.. _CONFIG_GDB_REMOTE_SERIAL_EXT_NOTIF_PREFIX_STR:

The value of this option depends on the string the GDB client use to
prefix the notification packets.



:Symbol:           GDB_REMOTE_SERIAL_EXT_NOTIF_PREFIX_STR
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Trigger string for remote serial ext. via notifi. packets" if GDB_SERVER (value: "n")
:Default values:

 *  "WrCons"
 *   Condition: GDB_SERVER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/debug/Kconfig:112