:orphan:

.. title:: GPIO_DW_2_IRQ_SHARED_NAME

.. option:: CONFIG_GPIO_DW_2_IRQ_SHARED_NAME:
.. _CONFIG_GPIO_DW_2_IRQ_SHARED_NAME:

Specify the device name for the shared IRQ driver. It is used to register
this driver with the shared IRQ driver, so interrupts can be dispatched
correctly.



:Symbol:           GPIO_DW_2_IRQ_SHARED_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Shared IRQ" if GPIO_DW_2_IRQ_SHARED (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_DW && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.dw:189