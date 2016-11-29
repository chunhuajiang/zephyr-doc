:orphan:

.. title:: BMG160_INT_PIN

.. option:: CONFIG_BMG160_INT_PIN:
.. _CONFIG_BMG160_INT_PIN:

BMG160 interrupt pin.



:Symbol:           BMG160_INT_PIN
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "BMG160 INT PIN" if BMG160 && BMG160_TRIGGER (value: "n")
:Default values:

 *  2 (value: "n")
 *   Condition: BMG160 && BMG160_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/bmg160/Kconfig:92