:orphan:

.. title:: GPIO_CMSDK_AHB_PORT1_DEV_NAME

.. option:: CONFIG_GPIO_CMSDK_AHB_PORT1_DEV_NAME:
.. _CONFIG_GPIO_CMSDK_AHB_PORT1_DEV_NAME:

Device name for Port 1.



:Symbol:           GPIO_CMSDK_AHB_PORT1_DEV_NAME
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Device name for Port 1" if GPIO_CMSDK_AHB_PORT1 (value: "n")
:Default values:

 *  "GPIO_1"
 *   Condition: GPIO_CMSDK_AHB_PORT1 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_CMSDK_AHB && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.cmsdk_ahb:62