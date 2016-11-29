:orphan:

.. title:: MCP9808_GPIO_PIN

.. option:: CONFIG_MCP9808_GPIO_PIN:
.. _CONFIG_MCP9808_GPIO_PIN:

The GPIO pin the MCP9808 interrupt is connected to.



:Symbol:           MCP9808_GPIO_PIN
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO pin for MCP9808 interrupt" if MCP9808 && MCP9808_TRIGGER (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: MCP9808 && MCP9808_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/mcp9808/Kconfig:78