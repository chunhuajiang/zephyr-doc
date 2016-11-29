:orphan:

.. title:: HP206C_ALT_OFFSET

.. option:: CONFIG_HP206C_ALT_OFFSET:
.. _CONFIG_HP206C_ALT_OFFSET:

Value, in cm, that will be used to compensate altitude calculation.
For more info on how to choose this value, consult section 6.1.1 in
the datasheet.


:Symbol:           HP206C_ALT_OFFSET
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Altitude offset (in cm)" if HP206C && !HP206C_ALT_OFFSET_RUNTIME (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: HP206C && !HP206C_ALT_OFFSET_RUNTIME (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/hp206c/Kconfig:57