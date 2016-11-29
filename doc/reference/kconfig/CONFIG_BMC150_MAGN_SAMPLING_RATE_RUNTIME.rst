:orphan:

.. title:: BMC150_MAGN_SAMPLING_RATE_RUNTIME

.. option:: CONFIG_BMC150_MAGN_SAMPLING_RATE_RUNTIME:
.. _CONFIG_BMC150_MAGN_SAMPLING_RATE_RUNTIME:

Enable alteration of sampling rate attribute at runtime.



:Symbol:           BMC150_MAGN_SAMPLING_RATE_RUNTIME
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable dynamic sampling rate" if BMC150_MAGN (value: "n")
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
 * ../drivers/sensor/bmc150_magn/Kconfig:78