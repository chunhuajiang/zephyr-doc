:orphan:

.. title:: BLUETOOTH_NRF51_PM

.. option:: CONFIG_BLUETOOTH_NRF51_PM:
.. _CONFIG_BLUETOOTH_NRF51_PM:

Power Management support for Nordic BLE nRF51 chip. Allows to enable,
disable the chip and handle wakeups.



:Symbol:           BLUETOOTH_NRF51_PM
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "nRF51 Power Management [EXPERIMENTAL]" if BLUETOOTH_H4 || NBLE (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NBLE && BOARD_QUARK_SE_C1000_DEVBOARD (value: "n")
:Locations:
 * ../drivers/bluetooth/Kconfig:35
 * ../boards/x86/arduino_101/Kconfig.defconfig:24
 * ../boards/x86/quark_se_c1000_devboard/Kconfig.defconfig:12