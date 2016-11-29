:orphan:

.. title:: STDOUT_CONSOLE

.. option:: CONFIG_STDOUT_CONSOLE:
.. _CONFIG_STDOUT_CONSOLE:

This option directs standard output (e.g. printf) to the console
device, rather than suppressing it entirely.



:Symbol:           STDOUT_CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Send stdout to console" if CONSOLE_HAS_DRIVER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: CONSOLE_HAS_DRIVER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING_WITH_LOGGING && NETWORKING || NET_BUF_DEBUG && NET_BUF || NET_BUF_SIMPLE_DEBUG && NET_BUF_DEBUG || BLUETOOTH_HCI && BLUETOOTH && BLUETOOTH_DEBUG_LOG (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:195