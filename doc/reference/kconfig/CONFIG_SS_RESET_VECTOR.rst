:orphan:

.. title:: SS_RESET_VECTOR

.. option:: CONFIG_SS_RESET_VECTOR:
.. _CONFIG_SS_RESET_VECTOR:

Sensor subsystem reset vector. This value is needed to init the ARC
system on the SoC.



:Symbol:           SS_RESET_VECTOR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Sensor Subsystem Reset Vector"
:Default values:

 *  0x40000000 (value: "n")
 *   Condition: (none)
 *  0x40034000 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig:28
 * ../boards/x86/arduino_101/Kconfig.defconfig:10