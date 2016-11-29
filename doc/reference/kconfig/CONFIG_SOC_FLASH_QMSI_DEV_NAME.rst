:orphan:

.. title:: SOC_FLASH_QMSI_DEV_NAME

.. option:: CONFIG_SOC_FLASH_QMSI_DEV_NAME:
.. _CONFIG_SOC_FLASH_QMSI_DEV_NAME:

Specify the device name for the flash driver.



:Symbol:           SOC_FLASH_QMSI_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI flash device name" if SOC_FLASH_QMSI (value: "n")
:Default values:

 *  "QUARK_FLASH"
 *   Condition: SOC_FLASH_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:94