:orphan:

.. title:: DATA_ENDIANNESS_LITTLE

.. option:: CONFIG_DATA_ENDIANNESS_LITTLE:
.. _CONFIG_DATA_ENDIANNESS_LITTLE:

This is driven by the processor implementation, since it is fixed in
hardware. The board should set this value to 'n' if the data is
implemented as big endian.



:Symbol:           DATA_ENDIANNESS_LITTLE
:Type:             bool
:Value:            "n"
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
 *   Condition: (none)
 *  y (value: "y")
 *   Condition: (none)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 CPU_CORTEX_M && ARM && CPU_CORTEX_M (value: "n")
:Locations:
 * ../arch/arc/Kconfig:69
 * ../arch/arm/core/cortex_m/Kconfig:110