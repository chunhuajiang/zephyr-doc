:orphan:

.. title:: GPIO_DW_0_IRQ_SHARED_NAME

.. option:: CONFIG_GPIO_DW_0_IRQ_SHARED_NAME:
.. _CONFIG_GPIO_DW_0_IRQ_SHARED_NAME:

Specify the device name for the shared IRQ driver. It is used to register
this driver with the shared IRQ driver, so interrupts can be dispatched
correctly.



:Symbol:           GPIO_DW_0_IRQ_SHARED_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Shared IRQ" if GPIO_DW_0 && GPIO_DW_0_IRQ_SHARED (value: "n")
:Default values:

 *  SHARED_IRQ_0_NAME (value: "")
 *   Condition: SHARED_IRQ (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO && SOC_SERIES_QUARK_X1000 && GPIO_DW && GPIO_DW_0 (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:89
 * ../arch/x86/soc/intel_quark/quark_x1000/Kconfig.defconfig.series:149