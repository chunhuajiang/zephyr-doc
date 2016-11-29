:orphan:

.. title:: PORT_K64_INT_STATUS_OFFSET

.. option:: CONFIG_PORT_K64_INT_STATUS_OFFSET:
.. _CONFIG_PORT_K64_INT_STATUS_OFFSET:

The configuration item CONFIG_PORT_K64_INT_STATUS_OFFSET:

:Symbol:           PORT_K64_INT_STATUS_OFFSET
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Freescale K64-based Port Control interrupt status register offset" if GPIO_K64 (value: "n")
:Default values:

 *  0xA0 (value: "n")
 *   Condition: GPIO_K64 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 GPIO_K64 && GPIO (value: "n")
:Locations:
 * ../drivers/gpio/Kconfig.k64:29