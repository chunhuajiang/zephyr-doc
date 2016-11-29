:orphan:

.. title:: MCP9808_THREAD_STACK_SIZE

.. option:: CONFIG_MCP9808_THREAD_STACK_SIZE:
.. _CONFIG_MCP9808_THREAD_STACK_SIZE:

The configuration item CONFIG_MCP9808_THREAD_STACK_SIZE:

:Symbol:           MCP9808_THREAD_STACK_SIZE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Sensor delayed work thread stack size" if MCP9808 && MCP9808_TRIGGER_OWN_THREAD (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: MCP9808 && MCP9808_TRIGGER_OWN_THREAD (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:85