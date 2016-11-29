:orphan:

.. title:: PWM_QMSI_NUM_PORTS

.. option:: CONFIG_PWM_QMSI_NUM_PORTS:
.. _CONFIG_PWM_QMSI_NUM_PORTS:

Specify how many PWM ports on the IP block.



:Symbol:           PWM_QMSI_NUM_PORTS
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Number of PWM ports for PWM" if PWM_QMSI (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: PWM_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.qmsi:35