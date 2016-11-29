:orphan:

.. title:: MCP9808_I2C_ADDR

.. option:: CONFIG_MCP9808_I2C_ADDR:
.. _CONFIG_MCP9808_I2C_ADDR:

Specify the I2C slave address for the MCP9808.



:Symbol:           MCP9808_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "MCP9808 I2C slave address" if MCP9808 (value: "n")
:Default values:

 *  0x18 (value: "n")
 *   Condition: MCP9808 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:32