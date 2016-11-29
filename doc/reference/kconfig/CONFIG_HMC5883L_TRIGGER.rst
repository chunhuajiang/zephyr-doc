:orphan:

.. title:: HMC5883L_TRIGGER

.. option:: CONFIG_HMC5883L_TRIGGER:
.. _CONFIG_HMC5883L_TRIGGER:

The configuration item CONFIG_HMC5883L_TRIGGER:

:Symbol:           HMC5883L_TRIGGER
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
 HMC5883L_TRIGGER_GLOBAL_THREAD && GPIO || HMC5883L_TRIGGER_OWN_THREAD && GPIO (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:67