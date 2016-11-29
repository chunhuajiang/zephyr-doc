:orphan:

.. title:: SYS_LOG

.. option:: CONFIG_SYS_LOG:
.. _CONFIG_SYS_LOG:

Global switch for logging, when turned off log calls will not be
executed.



:Symbol:           SYS_LOG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable Logging" if PRINTK || STDOUT_CONSOLE (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PRINTK || STDOUT_CONSOLE (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NET_BUF_DEBUG && NET_BUF || NET_BUF_SIMPLE_DEBUG && NET_BUF_DEBUG || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_LOG (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:266