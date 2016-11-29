:orphan:

.. title:: BMG160_I2C_PORT_NAME

.. option:: CONFIG_BMG160_I2C_PORT_NAME:
.. _CONFIG_BMG160_I2C_PORT_NAME:

Master I2C port name through which BMG160 chip is accessed.



:Symbol:           BMG160_I2C_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master controller port name" if BMG160 (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: BMG160 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:16