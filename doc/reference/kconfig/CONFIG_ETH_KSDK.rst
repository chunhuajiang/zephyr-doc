:orphan:

.. title:: ETH_KSDK

.. option:: CONFIG_ETH_KSDK:
.. _CONFIG_ETH_KSDK:

Enable KSDK Ethernet driver.  Note, this driver performs one shot PHY
setup.  There is no support for PHY disconnect, reconnect or
configuration change.



:Symbol:           ETH_KSDK
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "KSDK Ethernet driver" if ETHERNET && HAS_KSDK (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ETHERNET && HAS_KSDK (value: "n")
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_MK64F12 && SOC_SERIES_KINETIS_K6X && ETHERNET (value: "n")
:Locations:
 * ../drivers/ethernet/Kconfig.ksdk:17
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.defconfig.mk64f12:68