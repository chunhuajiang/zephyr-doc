:orphan:

.. title:: QMSI_LIBRARY

.. option:: CONFIG_QMSI_LIBRARY:
.. _CONFIG_QMSI_LIBRARY:

This option enables QMSI device drivers. These drivers are actually shim
drivers based on drivers provided by QMSI BSP. The BSP provides a static
library (libqmsi) which implements several drivers for peripherals from
Intel MCUs (e.g. Quark SE and Quark D2000).



:Symbol:           QMSI_LIBRARY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable QMSI drivers using external library"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:

 *  :option:`CONFIG_QMSI`
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_QMSI (value: "n")
:Locations:
 * ../ext/hal/qmsi/Kconfig:39