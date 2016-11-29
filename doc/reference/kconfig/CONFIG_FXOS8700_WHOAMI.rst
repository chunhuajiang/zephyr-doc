:orphan:

.. title:: FXOS8700_WHOAMI

.. option:: CONFIG_FXOS8700_WHOAMI:
.. _CONFIG_FXOS8700_WHOAMI:

The datasheet defines the value of the WHOAMI register, but some
pre-production devices can have a different value. It is unlikely you
should need to change this configuration option from the default.



:Symbol:           FXOS8700_WHOAMI
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Ranges:

 *  [0x00, 0xff]
:Prompts:

 *  "WHOAMI value" if FXOS8700 (value: "n")
:Default values:

 *  0xc7 (value: "n")
 *   Condition: FXOS8700 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/fxos8700/Kconfig:63