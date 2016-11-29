:orphan:

.. title:: QMSI_INSTALL_PATH

.. option:: CONFIG_QMSI_INSTALL_PATH:
.. _CONFIG_QMSI_INSTALL_PATH:

This option holds the path where the QMSI library and headers are
installed. Make sure this option is properly set when QMSI_LIBRARY
is enabled otherwise the build will fail.



:Symbol:           QMSI_INSTALL_PATH
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI install path" if QMSI_LIBRARY (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 HAS_QMSI (value: "n")
:Locations:
 * ../ext/hal/qmsi/Kconfig:49