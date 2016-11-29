:orphan:

.. title:: HTS221_TRIGGER

.. option:: CONFIG_HTS221_TRIGGER:
.. _CONFIG_HTS221_TRIGGER:

The configuration item CONFIG_HTS221_TRIGGER:

:Symbol:           HTS221_TRIGGER
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
 HTS221_TRIGGER_GLOBAL_THREAD && GPIO || HTS221_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hts221/Kconfig:67