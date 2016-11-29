:orphan:

.. title:: SOC_FLASH_NRF5_DEV_NAME

.. option:: CONFIG_SOC_FLASH_NRF5_DEV_NAME:
.. _CONFIG_SOC_FLASH_NRF5_DEV_NAME:

Specify the device name for the flash driver.



:Symbol:           SOC_FLASH_NRF5_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Nordic nRF5X flash device name" if SOC_FLASH_NRF5 (value: "n")
:Default values:

 *  "NRF5_FLASH"
 *   Condition: SOC_FLASH_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:128