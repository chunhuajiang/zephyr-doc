:orphan:

.. title:: BMC150_MAGN_TRIGGER_THREAD_STACK

.. option:: CONFIG_BMC150_MAGN_TRIGGER_THREAD_STACK:
.. _CONFIG_BMC150_MAGN_TRIGGER_THREAD_STACK:

Specify the internal thread stack size.



:Symbol:           BMC150_MAGN_TRIGGER_THREAD_STACK
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Thread stack size" if BMC150_MAGN_TRIGGER (value: "n")
:Default values:

 *  1024 (value: "n")
 *   Condition: BMC150_MAGN_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmc150_magn/Kconfig:108