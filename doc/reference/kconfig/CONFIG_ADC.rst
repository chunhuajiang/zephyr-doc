:orphan:

.. title:: ADC

.. option:: CONFIG_ADC:
.. _CONFIG_ADC:

Enable ADC (Analog to Digital Converter) driver configuration



:Symbol:           ADC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "ADC drivers"
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
 * ../drivers/adc/Kconfig:22
 * ../boards/x86/galileo/Kconfig.defconfig:22