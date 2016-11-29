:orphan:

.. title:: TEXT_SECTION_OFFSET

.. option:: CONFIG_TEXT_SECTION_OFFSET:
.. _CONFIG_TEXT_SECTION_OFFSET:

This sets and offset before the text section and allows booting images
with custom headers that are inserted at the beginning of the image.



:Symbol:           TEXT_SECTION_OFFSET
:Type:             hex
:Value:            "0"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "TEXT section offset"
:Default values:

 *  0 (value: "n")
 *   Condition: (none)
 *  0x30 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BOARD_ARDUINO_101 (value: "n")
:Locations:
 * ../misc/Kconfig:27
 * ../boards/x86/arduino_101/Kconfig.defconfig:7