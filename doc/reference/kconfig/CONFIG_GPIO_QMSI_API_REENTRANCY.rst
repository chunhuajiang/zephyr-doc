:orphan:

.. title:: GPIO_QMSI_API_REENTRANCY

.. option:: CONFIG_GPIO_QMSI_API_REENTRANCY:
.. _CONFIG_GPIO_QMSI_API_REENTRANCY:

Enable support for QMSI GPIO driver API reentrancy.



:Symbol:           GPIO_QMSI_API_REENTRANCY
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO driver API reentrancy" if GPIO_QMSI (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: GPIO_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (GPIO_QMSI || GPIO_QMSI_SS) && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:45