:orphan:

.. title:: AON_API_REENTRANCY

.. option:: CONFIG_AON_API_REENTRANCY:
.. _CONFIG_AON_API_REENTRANCY:

Enable support for AON driver API reentrancy.


:Symbol:           AON_API_REENTRANCY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "AON driver API reentrancy" if AON_TIMER_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: AON_TIMER_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/counter/Kconfig:61