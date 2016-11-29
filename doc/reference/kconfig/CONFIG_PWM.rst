:orphan:

.. title:: PWM

.. option:: CONFIG_PWM:
.. _CONFIG_PWM:

Enable config options for PWM drivers.



:Symbol:           PWM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PWM (Pulse Width Modulation) Drivers"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig:19
 * ../boards/x86/galileo/Kconfig.defconfig:16