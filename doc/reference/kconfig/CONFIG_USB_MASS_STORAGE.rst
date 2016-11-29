:orphan:

.. title:: USB_MASS_STORAGE

.. option:: CONFIG_USB_MASS_STORAGE:
.. _CONFIG_USB_MASS_STORAGE:

USB Mass Storage device class driver



:Symbol:           USB_MASS_STORAGE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "USB Mass Storage Device Class Driver"
:Default values:

 *  n (value: "n")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 USB_DEVICE_STACK && USB_DEVICE_STACK (value: "n")
:Locations:
 * ../subsys/usb/class/Kconfig:55