:orphan:

.. title:: BMC150_MAGN_SAMPLING_REP_XY

.. option:: CONFIG_BMC150_MAGN_SAMPLING_REP_XY:
.. _CONFIG_BMC150_MAGN_SAMPLING_REP_XY:

Enable alteration of XY oversampling at runtime.



:Symbol:           BMC150_MAGN_SAMPLING_REP_XY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dynamic XY oversampling" if BMC150_MAGN (value: "n")
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
 * ../drivers/sensor/bmc150_magn/Kconfig:85