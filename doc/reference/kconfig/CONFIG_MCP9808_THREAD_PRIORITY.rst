:orphan:

.. title:: MCP9808_THREAD_PRIORITY

.. option:: CONFIG_MCP9808_THREAD_PRIORITY:
.. _CONFIG_MCP9808_THREAD_PRIORITY:

The configuration item CONFIG_MCP9808_THREAD_PRIORITY:

:Symbol:           MCP9808_THREAD_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "MCP9808 thread priority" if MCP9808 && MCP9808_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  10 (value: "n")
 *   Condition: MCP9808 && MCP9808_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:90