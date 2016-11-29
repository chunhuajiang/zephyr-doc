:orphan:

.. title:: PRESERVE_JTAG_IO_PINS

.. option:: CONFIG_PRESERVE_JTAG_IO_PINS:
.. _CONFIG_PRESERVE_JTAG_IO_PINS:

The FRDM-K64F board routes the PTA0/1/2 pins as JTAG/SWD signals that
are used for the OpenSDAv2 debug interface.  These pins are also routed to
the Arduino header as D8, D3 and D5, respectively.
Enable this option to preserve these pins for the debug interface.



:Symbol:           PRESERVE_JTAG_IO_PINS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Kinetis K6x JTAG pin usage" if PINMUX (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: PINMUX (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 SOC_SERIES_KINETIS_K6X && ARM (value: "n")
:Locations:
 * ../arch/arm/soc/nxp_kinetis/k6x/Kconfig.soc:117