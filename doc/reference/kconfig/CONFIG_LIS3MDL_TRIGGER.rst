:orphan:

.. title:: LIS3MDL_TRIGGER

.. option:: CONFIG_LIS3MDL_TRIGGER:
.. _CONFIG_LIS3MDL_TRIGGER:

The configuration item CONFIG_LIS3MDL_TRIGGER:

:Symbol:           LIS3MDL_TRIGGER
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
 LIS3MDL_TRIGGER_GLOBAL_THREAD && GPIO || LIS3MDL_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lis3mdl/Kconfig:77