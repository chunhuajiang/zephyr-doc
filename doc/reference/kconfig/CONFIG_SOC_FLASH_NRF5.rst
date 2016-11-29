:orphan:

.. title:: SOC_FLASH_NRF5

.. option:: CONFIG_SOC_FLASH_NRF5:
.. _CONFIG_SOC_FLASH_NRF5:

Enables Nordic Semiconductor nRF5X flash driver.



:Symbol:           SOC_FLASH_NRF5
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Nordic Semiconductor nRF5X flash driver" if FLASH && SOC_FAMILY_NRF5 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: FLASH && SOC_FAMILY_NRF5 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:121