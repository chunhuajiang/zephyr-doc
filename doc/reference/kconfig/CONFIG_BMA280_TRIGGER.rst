:orphan:

.. title:: BMA280_TRIGGER

.. option:: CONFIG_BMA280_TRIGGER:
.. _CONFIG_BMA280_TRIGGER:

The configuration item CONFIG_BMA280_TRIGGER:

:Symbol:           BMA280_TRIGGER
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
 BMA280_TRIGGER_GLOBAL_THREAD && GPIO || BMA280_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bma280/Kconfig:105