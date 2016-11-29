:orphan:

.. title:: BOARD_GALILEO

.. option:: CONFIG_BOARD_GALILEO:
.. _CONFIG_BOARD_GALILEO:

The Intel Galileo Gen 2 development board is a microcontroller board
based on the Intel Quark SoC X1000 application processor, a 32-bit
Intel® Pentium® brand system on a chip (SoC). It is the first board
based on Intel architecture designed to be hardware and software
pin-compatible with shields designed for the Arduino Uno* R3.


:Symbol:           BOARD_GALILEO
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Galileo Gen2" if SOC_SERIES_QUARK_X1000 (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../boards/x86/galileo/Kconfig.board:2