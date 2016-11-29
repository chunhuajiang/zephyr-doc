:orphan:

.. title:: HP206C_OSR

.. option:: CONFIG_HP206C_OSR:
.. _CONFIG_HP206C_OSR:

Allowed values: 4096, 2048, 1024, 512, 256, 128



:Symbol:           HP206C_OSR
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Oversampling rate" if HP206C && !HP206C_OSR_RUNTIME (value: "n")
:Default values:

 *  4096 (value: "n")
 *   Condition: HP206C && !HP206C_OSR_RUNTIME (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hp206c/Kconfig:45