:orphan:

.. title:: NBLE

.. option:: CONFIG_NBLE:
.. _CONFIG_NBLE:

Note: This feature is deprecated and will be removed in a
future Zephyr version.

Enables support for using Nordic Semiconductor nRF51 Bluetooth
LE chips with a custom firmware. The API for this is a subset of
the normal Bluetooth API (include/bluetooth/). This driver can
only be enabled if CONFIG_BLUETOOTH has not been enabled.

A fundamental assumption that the driver makes is that it is
run on an architecture with the same ABI (e.g. struct packing
& endianess) as the nRF51 chip. The driver cannot be used on
any architecture that doesn't fulfill this requirement.



:Symbol:           NBLE
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Support for custom non-HCI nRF51 firmware [DEPRECATED]" if SERIAL (value: "n")
:Default values:
 (no default values)
:Selects:

 *  :option:`CONFIG_UART_INTERRUPT_DRIVEN` if SERIAL (value: "n")
 *  :option:`CONFIG_NANO_TIMEOUTS` if SERIAL (value: "n")
 *  :option:`CONFIG_NET_BUF` if SERIAL (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 BLUETOOTH_CUSTOM && BLUETOOTH (value: "n")
:Locations:
 * ../drivers/bluetooth/nble/Kconfig:19