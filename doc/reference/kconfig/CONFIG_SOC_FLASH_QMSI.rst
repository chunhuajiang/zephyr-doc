:orphan:

.. title:: SOC_FLASH_QMSI

.. option:: CONFIG_SOC_FLASH_QMSI:
.. _CONFIG_SOC_FLASH_QMSI:

Enable QMSI quark flash driver.



:Symbol:           SOC_FLASH_QMSI
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "QMSI flash driver" if QMSI && FLASH (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: QMSI && FLASH (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:86