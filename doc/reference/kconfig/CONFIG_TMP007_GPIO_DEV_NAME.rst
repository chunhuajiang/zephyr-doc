:orphan:

.. title:: TMP007_GPIO_DEV_NAME

.. option:: CONFIG_TMP007_GPIO_DEV_NAME:
.. _CONFIG_TMP007_GPIO_DEV_NAME:

The device name of the GPIO device to which the TMP007 interrupt
(alert) pin is connected.



:Symbol:           TMP007_GPIO_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "GPIO device" if TMP007 && TMP007_TRIGGER (value: "n")
:Default values:

 *  "GPIO_0"
 *   Condition: TMP007 && TMP007_TRIGGER (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/tmp007/Kconfig:90