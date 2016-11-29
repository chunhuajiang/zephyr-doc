:orphan:

.. title:: IS_BOOTLOADER

.. option:: CONFIG_IS_BOOTLOADER:
.. _CONFIG_IS_BOOTLOADER:

This option indicates that Zephyr will act as a bootloader to execute
a separate Zephyr image payload.



:Symbol:           IS_BOOTLOADER
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Act as a bootloader" if XIP && ARM (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: XIP && ARM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:362