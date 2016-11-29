:orphan:

.. title:: GPIO_QMSI_0_NAME

.. option:: CONFIG_GPIO_QMSI_0_NAME:
.. _CONFIG_GPIO_QMSI_0_NAME:

The configuration item CONFIG_GPIO_QMSI_0_NAME:

:Symbol:           GPIO_QMSI_0_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Driver name" if GPIO_QMSI_0 (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: GPIO_QMSI_0 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (GPIO_QMSI || GPIO_QMSI_SS) && GPIO && GPIO_QMSI (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:61