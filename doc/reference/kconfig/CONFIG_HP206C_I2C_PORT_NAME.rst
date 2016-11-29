:orphan:

.. title:: HP206C_I2C_PORT_NAME

.. option:: CONFIG_HP206C_I2C_PORT_NAME:
.. _CONFIG_HP206C_I2C_PORT_NAME:

Master I2C port name through which HP206C chip is accessed.



:Symbol:           HP206C_I2C_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C master controller port name" if HP206C (value: "n")
:Default values:

 *  "I2C_0"
 *   Condition: HP206C (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hp206c/Kconfig:33