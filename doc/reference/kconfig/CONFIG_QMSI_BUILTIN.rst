:orphan:

.. title:: QMSI_BUILTIN

.. option:: CONFIG_QMSI_BUILTIN:
.. _CONFIG_QMSI_BUILTIN:

Link with local QMSI sources instead of external library.



:Symbol:           QMSI_BUILTIN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable QMSI drivers through integrated sources"
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
 * ../ext/hal/qmsi/Kconfig:32