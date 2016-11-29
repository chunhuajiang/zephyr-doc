:orphan:

.. title:: SOC_WATCH

.. option:: CONFIG_SOC_WATCH:
.. _CONFIG_SOC_WATCH:

This option enables the SoCWatch driver and related instrumentation.



:Symbol:           SOC_WATCH
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable SoCWatch drivers and related instrumentation" if KERNEL_EVENT_LOGGER (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: KERNEL_EVENT_LOGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_QMSI (value: "n")
:Locations:
 * ../ext/hal/qmsi/Kconfig:57