:orphan:

.. title:: USB_CDC_ACM

.. option:: CONFIG_USB_CDC_ACM:
.. _CONFIG_USB_CDC_ACM:

USB CDC ACM device class driver



:Symbol:           USB_CDC_ACM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "USB CDC ACM Device Class Driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 SERIAL && CONSOLE && USB_UART_CONSOLE (value: "n")
:Additional dependencies from enclosing menus and ifs:
 USB_DEVICE_STACK && USB_DEVICE_STACK (value: "n")
:Locations:
 * ../subsys/usb/class/Kconfig:21