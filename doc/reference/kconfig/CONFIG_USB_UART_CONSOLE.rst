:orphan:

.. title:: USB_UART_CONSOLE

.. option:: CONFIG_USB_UART_CONSOLE:
.. _CONFIG_USB_UART_CONSOLE:

Enable this option to use the USB UART for console output. The output
can be viewed from the USB host via /dev/ttyACM* port. Note that console
inputs from the USB UART are not functional yet. Also since the USB
layer currently doesnt support multiple interfaces, this shouldnt be
selected in conjunction with say USB Mass Storage.



:Symbol:           USB_UART_CONSOLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Use USB port for console outputs" if SERIAL (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SERIAL (value: "n")
:Selects:

 *  :option:`CONFIG_CONSOLE_HAS_DRIVER` if SERIAL (value: "n")
 *  :option:`CONFIG_USB_CDC_ACM` if SERIAL (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CONSOLE (value: "n")
:Locations:
 * ../drivers/console/Kconfig:98