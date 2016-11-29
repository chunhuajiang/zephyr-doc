:orphan:

.. title:: LPS25HB_SAMPLING_RATE

.. option:: CONFIG_LPS25HB_SAMPLING_RATE:
.. _CONFIG_LPS25HB_SAMPLING_RATE:

Sensor output data rate expressed in samples per second.
Data rates supported by the chip are 1, 7, 13, 25.



:Symbol:           LPS25HB_SAMPLING_RATE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Output data rate" if LPS25HB (value: "n")
:Default values:

 *  25 (value: "n")
 *   Condition: LPS25HB (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 LPS25HB (value: "n")
:Locations:
 * ../drivers/sensor/lps25hb/Kconfig:76