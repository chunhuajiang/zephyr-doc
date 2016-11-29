:orphan:

.. title:: GPIO_QMSI_INIT_PRIORITY

.. option:: CONFIG_GPIO_QMSI_INIT_PRIORITY:
.. _CONFIG_GPIO_QMSI_INIT_PRIORITY:

Device driver initialization priority.



:Symbol:           GPIO_QMSI_INIT_PRIORITY
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Init priority" if GPIO_QMSI (value: "n")
:Default values:

 *  60 (value: "n")
 *   Condition: GPIO_QMSI (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (GPIO_QMSI || GPIO_QMSI_SS) && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.qmsi:37