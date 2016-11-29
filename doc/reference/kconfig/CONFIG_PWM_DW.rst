:orphan:

.. title:: PWM_DW

.. option:: CONFIG_PWM_DW:
.. _CONFIG_PWM_DW:

Enable driver to utilize PWM on the DesignWare Timer IP block.
Care must be taken if one is also to use the timer feature, as
they both use the same set of registers.



:Symbol:           PWM_DW
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DesignWare PWM" if PWM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: PWM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.dw:19