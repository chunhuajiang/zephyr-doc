:orphan:

.. title:: SOC_FLASH_QMSI_WAIT_STATES

.. option:: CONFIG_SOC_FLASH_QMSI_WAIT_STATES:
.. _CONFIG_SOC_FLASH_QMSI_WAIT_STATES:

Specify the number of wait states for quark flash.



:Symbol:           SOC_FLASH_QMSI_WAIT_STATES
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "The number of flash wait states" if SOC_FLASH_QMSI (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: SOC_FLASH_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/flash/Kconfig:108