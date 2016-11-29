:orphan:

.. title:: PWM_DW_0_DRV_NAME

.. option:: CONFIG_PWM_DW_0_DRV_NAME:
.. _CONFIG_PWM_DW_0_DRV_NAME:

Specify the device name for the DesignWare PWM driver.



:Symbol:           PWM_DW_0_DRV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DesignWare PWM Device Name" if PWM_DW (value: "n")
:Default values:

 *  "PWM_0"
 *   Condition: PWM_DW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 PWM_DW && PWM (value: "n")
:Locations:
 * ../drivers/pwm/Kconfig.dw:30