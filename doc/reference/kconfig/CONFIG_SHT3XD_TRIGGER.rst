:orphan:

.. title:: SHT3XD_TRIGGER

.. option:: CONFIG_SHT3XD_TRIGGER:
.. _CONFIG_SHT3XD_TRIGGER:

The configuration item CONFIG_SHT3XD_TRIGGER:

:Symbol:           SHT3XD_TRIGGER
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
 SHT3XD_TRIGGER_GLOBAL_THREAD && GPIO || SHT3XD_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/sht3xd/Kconfig:79