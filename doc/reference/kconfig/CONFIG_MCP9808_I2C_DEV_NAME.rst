:orphan:

.. title:: MCP9808_I2C_DEV_NAME

.. option:: CONFIG_MCP9808_I2C_DEV_NAME:
.. _CONFIG_MCP9808_I2C_DEV_NAME:

Specify the device name of the I2C master device to which MCP9808 is
connected.



:Symbol:           MCP9808_I2C_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master where MCP9808 is connected" if MCP9808 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: MCP9808 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:39