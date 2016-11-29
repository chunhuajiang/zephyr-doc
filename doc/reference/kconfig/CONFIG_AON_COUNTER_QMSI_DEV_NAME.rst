:orphan:

.. title:: AON_COUNTER_QMSI_DEV_NAME

.. option:: CONFIG_AON_COUNTER_QMSI_DEV_NAME:
.. _CONFIG_AON_COUNTER_QMSI_DEV_NAME:

Specify the device name for AON counter driver.



:Symbol:           AON_COUNTER_QMSI_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI AON Counter Device Name" if AON_COUNTER_QMSI (value: "n")
:Default values:

 *  "AON_COUNTER"
 *   Condition: AON_COUNTER_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/counter/Kconfig:33