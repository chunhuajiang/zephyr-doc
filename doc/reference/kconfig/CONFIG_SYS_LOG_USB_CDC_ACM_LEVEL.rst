:orphan:

.. title:: SYS_LOG_USB_CDC_ACM_LEVEL

.. option:: CONFIG_SYS_LOG_USB_CDC_ACM_LEVEL:
.. _CONFIG_SYS_LOG_USB_CDC_ACM_LEVEL:

Sets log level for USB CDC ACM device class driver

Levels are:

- 0 OFF, do not write

- 1 ERROR, only write SYS_LOG_ERR

- 2 WARNING, write SYS_LOG_WRN in adition to previous level

- 3 INFO, write SYS_LOG_INF in adition to previous levels

- 4 DEBUG, write SYS_LOG_DBG in adition to previous levels



:Symbol:           SYS_LOG_USB_CDC_ACM_LEVEL
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "USB CDC ACM device class driver log level" if USB_CDC_ACM (value: "n")
:Default values:

 *  0 (value: "n")
 *   Condition: USB_CDC_ACM (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 USB_DEVICE_STACK && USB_DEVICE_STACK (value: "n")
:Locations:
 * ../subsys/usb/class/Kconfig:35