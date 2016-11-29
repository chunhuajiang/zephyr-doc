:orphan:

.. title:: ISL29035_TRIGGER

.. option:: CONFIG_ISL29035_TRIGGER:
.. _CONFIG_ISL29035_TRIGGER:

The configuration item CONFIG_ISL29035_TRIGGER:

:Symbol:           ISL29035_TRIGGER
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
 ISL29035_TRIGGER_GLOBAL_THREAD && GPIO || ISL29035_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/isl29035/Kconfig:152