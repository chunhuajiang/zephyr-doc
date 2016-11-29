:orphan:

.. title:: LPS25HB_I2C_ADDR

.. option:: CONFIG_LPS25HB_I2C_ADDR:
.. _CONFIG_LPS25HB_I2C_ADDR:

I2C address of the LPS25HB sensor.
Use 0x5C if the SA0 pin is pulled to GND or 0x5D if the SA0
pin is pulled to VDD.



:Symbol:           LPS25HB_I2C_ADDR
:Type:             hex
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "I2C address" if LPS25HB (value: "n")
:Default values:

 *  "0x5C" (value: "n")
 *   Condition: LPS25HB (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../drivers/sensor/lps25hb/Kconfig:54