:orphan:

.. title:: PWM_QMSI_DEV_NAME

.. option:: CONFIG_PWM_QMSI_DEV_NAME:
.. _CONFIG_PWM_QMSI_DEV_NAME:

Specify the device name for the PWM driver.



:Symbol:           PWM_QMSI_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI PWM Device Name" if PWM_QMSI (value: "n")
:Default values:

 *  "PWM_0"
 *   Condition: PWM_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.qmsi:28