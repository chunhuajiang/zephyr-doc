:orphan:

.. title:: SHT3XD_TRIGGER_OWN_THREAD

.. option:: CONFIG_SHT3XD_TRIGGER_OWN_THREAD:
.. _CONFIG_SHT3XD_TRIGGER_OWN_THREAD:

The configuration item CONFIG_SHT3XD_TRIGGER_OWN_THREAD:

:Symbol:           SHT3XD_TRIGGER_OWN_THREAD
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use own thread" if GPIO (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_SHT3XD_TRIGGER` if GPIO (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:71