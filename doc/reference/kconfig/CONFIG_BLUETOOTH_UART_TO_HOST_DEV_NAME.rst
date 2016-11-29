:orphan:

.. title:: BLUETOOTH_UART_TO_HOST_DEV_NAME

.. option:: CONFIG_BLUETOOTH_UART_TO_HOST_DEV_NAME:
.. _CONFIG_BLUETOOTH_UART_TO_HOST_DEV_NAME:

This option specifies the name of UART device to be used
to connect to an external Bluetooth Host when Zephyr is
acting as a Bluetooth Controller.



:Symbol:           BLUETOOTH_UART_TO_HOST_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device Name of UART Device to an external Bluetooth Host" if BLUETOOTH_HCI_RAW (value: "n")
:Default values:

 *  "UART_0"
 *   Condition: BLUETOOTH_HCI_RAW (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_HCI && BLUETOOTH (value: "n")
:Locations:
 * ../subsys/bluetooth/host/Kconfig:75