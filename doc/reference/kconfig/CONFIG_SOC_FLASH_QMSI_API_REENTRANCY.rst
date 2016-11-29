:orphan:

.. title:: SOC_FLASH_QMSI_API_REENTRANCY

.. option:: CONFIG_SOC_FLASH_QMSI_API_REENTRANCY:
.. _CONFIG_SOC_FLASH_QMSI_API_REENTRANCY:

Enable support for QMSI flash driver API reentrancy.


:Symbol:           SOC_FLASH_QMSI_API_REENTRANCY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "flash driver API reentrancy for QMSI shim driver" if SOC_FLASH_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: SOC_FLASH_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:153