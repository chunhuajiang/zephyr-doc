:orphan:

.. title:: AON_TIMER_QMSI_DEV_NAME

.. option:: CONFIG_AON_TIMER_QMSI_DEV_NAME:
.. _CONFIG_AON_TIMER_QMSI_DEV_NAME:

Specify the device name for AON timer driver.



:Symbol:           AON_TIMER_QMSI_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI AON Timer Device Name" if AON_TIMER_QMSI (value: "n")
:Default values:

 *  "AON_TIMER"
 *   Condition: AON_TIMER_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/counter/Kconfig:48