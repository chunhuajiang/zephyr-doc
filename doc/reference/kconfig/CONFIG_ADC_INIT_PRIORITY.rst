:orphan:

.. title:: ADC_INIT_PRIORITY

.. option:: CONFIG_ADC_INIT_PRIORITY:
.. _CONFIG_ADC_INIT_PRIORITY:

ADC Device driver initialization priority.



:Symbol:           ADC_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if ADC (value: "n")
:Default values:

 *  80 (value: "n")
 *   Condition: ADC (value: "n")
 *  95 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_GALILEO (value: "n")
:Locations:
 * ../drivers/adc/Kconfig:51
 * ../boards/x86/galileo/Kconfig.defconfig:134