:orphan:

.. title:: REBOOT_RST_CNT

.. option:: CONFIG_REBOOT_RST_CNT:
.. _CONFIG_REBOOT_RST_CNT:

Reboot via the RST_CNT register, going back to BIOS.



:Symbol:           REBOOT_RST_CNT
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   true
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Reboot via RST_CNT register"
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 X86 (value: "y")
:Locations:
 * ../arch/x86/Kconfig:144