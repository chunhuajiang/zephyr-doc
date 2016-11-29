:orphan:

.. title:: TMP007_TRIGGER

.. option:: CONFIG_TMP007_TRIGGER:
.. _CONFIG_TMP007_TRIGGER:

The configuration item CONFIG_TMP007_TRIGGER:

:Symbol:           TMP007_TRIGGER
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
 TMP007_TRIGGER_GLOBAL_THREAD && GPIO || TMP007_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:86