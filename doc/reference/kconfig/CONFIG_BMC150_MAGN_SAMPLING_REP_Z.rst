:orphan:

.. title:: BMC150_MAGN_SAMPLING_REP_Z

.. option:: CONFIG_BMC150_MAGN_SAMPLING_REP_Z:
.. _CONFIG_BMC150_MAGN_SAMPLING_REP_Z:

Enable alteration of Z oversampling at runtime.



:Symbol:           BMC150_MAGN_SAMPLING_REP_Z
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dynamic Z oversampling" if BMC150_MAGN (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: BMC150_MAGN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BMC150_MAGN (value: "n")
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:92