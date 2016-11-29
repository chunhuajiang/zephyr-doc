:orphan:

.. title:: HMC5883L_TRIGGER_OWN_THREAD

.. option:: CONFIG_HMC5883L_TRIGGER_OWN_THREAD:
.. _CONFIG_HMC5883L_TRIGGER_OWN_THREAD:

The configuration item CONFIG_HMC5883L_TRIGGER_OWN_THREAD:

:Symbol:           HMC5883L_TRIGGER_OWN_THREAD
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

 *  :option:`CONFIG_HMC5883L_TRIGGER` if GPIO (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hmc5883l/Kconfig:59