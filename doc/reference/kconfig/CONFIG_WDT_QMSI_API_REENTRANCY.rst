:orphan:

.. title:: WDT_QMSI_API_REENTRANCY

.. option:: CONFIG_WDT_QMSI_API_REENTRANCY:
.. _CONFIG_WDT_QMSI_API_REENTRANCY:

Enable support for WDT shim driver API reentrancy.



:Symbol:           WDT_QMSI_API_REENTRANCY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "WDT shim driver API reentrancy" if WDT_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: WDT_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 WATCHDOG (value: "n")
:Locations:
 * ../drivers/watchdog/Kconfig:51