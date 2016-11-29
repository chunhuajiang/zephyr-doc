:orphan:

.. title:: MCP9808_TRIGGER

.. option:: CONFIG_MCP9808_TRIGGER:
.. _CONFIG_MCP9808_TRIGGER:

The configuration item CONFIG_MCP9808_TRIGGER:

:Symbol:           MCP9808_TRIGGER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 MCP9808_TRIGGER_GLOBAL_THREAD && GPIO || MCP9808_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:67