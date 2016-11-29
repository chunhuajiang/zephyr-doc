:orphan:

.. title:: BMC150_MAGN_TRIGGER

.. option:: CONFIG_BMC150_MAGN_TRIGGER:
.. _CONFIG_BMC150_MAGN_TRIGGER:

Enable triggers for BMC150 magnetometer



:Symbol:           BMC150_MAGN_TRIGGER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable triggers" if BMC150_MAGN && GPIO (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: BMC150_MAGN && GPIO (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:101