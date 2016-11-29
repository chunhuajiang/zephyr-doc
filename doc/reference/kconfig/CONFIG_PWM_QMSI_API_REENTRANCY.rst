:orphan:

.. title:: PWM_QMSI_API_REENTRANCY

.. option:: CONFIG_PWM_QMSI_API_REENTRANCY:
.. _CONFIG_PWM_QMSI_API_REENTRANCY:

Enable support for PWM shim driver API reentrancy.


:Symbol:           PWM_QMSI_API_REENTRANCY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PWM shim driver API reentrancy" if PWM_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.qmsi:42