:orphan:

.. title:: NANO_TIMEOUTS

.. option:: CONFIG_NANO_TIMEOUTS:
.. _CONFIG_NANO_TIMEOUTS:

Only here for common (ie. non-unified kernel) code that rely on this.
Unified kernel uses SYS_CLOCK_EXISTS everywhere instead.



:Symbol:           NANO_TIMEOUTS
:Type:             bool
:Value:            "y"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:
 (no prompts)
:Default values:

 *  y (value: "y")
 *   Condition: SYS_CLOCK_EXISTS (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 BLUETOOTH_CUSTOM && BLUETOOTH && SERIAL && NBLE || ADC_TI_ADC108S102 && ADC || NETWORKING (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../kernel/unified/Kconfig:160