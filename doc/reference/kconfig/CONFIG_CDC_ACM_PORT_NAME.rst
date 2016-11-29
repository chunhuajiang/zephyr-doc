:orphan:

.. title:: CDC_ACM_PORT_NAME

.. option:: CONFIG_CDC_ACM_PORT_NAME:
.. _CONFIG_CDC_ACM_PORT_NAME:

Port name through which CDC ACM class device driver is accessed



:Symbol:           CDC_ACM_PORT_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "CDC ACM class device driver port name" if USB_CDC_ACM (value: "n")
:Default values:

 *  "CDC_ACM"
 *   Condition: USB_CDC_ACM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 USB_DEVICE_STACK && USB_DEVICE_STACK (value: "n")
:Locations:
 * ../subsys/usb/class/Kconfig:28