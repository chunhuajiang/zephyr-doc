:orphan:

.. title:: QMSI

.. option:: CONFIG_QMSI:
.. _CONFIG_QMSI:

automatically set when either of QMSI_LIBRARY or QMSI_BUILTIN
is selected.



:Symbol:           QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI driver support" if HAS_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: HAS_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 QMSI_BUILTIN && HAS_QMSI || QMSI_LIBRARY && HAS_QMSI (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/hal/qmsi/Kconfig:22