:orphan:

.. title:: USB_DW_IRQ_PRI

.. option:: CONFIG_USB_DW_IRQ_PRI:
.. _CONFIG_USB_DW_IRQ_PRI:

USB interrupt priority.



:Symbol:           USB_DW_IRQ_PRI
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "DesignWare USB Driver Interrupt priority" if USB_DW (value: "n")
:Default values:

 *  3 (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 USB && SOC_SERIES_QUARK_SE (value: "n")
:Locations:
 * ../drivers/usb/device/Kconfig:28
 * ../arch/x86/soc/intel_quark/quark_se/Kconfig.defconfig.series:236